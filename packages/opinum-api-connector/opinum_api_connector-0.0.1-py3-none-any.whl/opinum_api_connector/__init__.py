import os
from oauthlib.oauth2 import LegacyApplicationClient
from requests_oauthlib import OAuth2Session
import json
import requests
import datetime as dt

DEFAULT_API_URL = 'https://api.opinum.com'
DEFAULT_AUTH_URL = 'https://identity.opinum.com'
DEFAULT_SCOPE = 'opisense-api push-data'
DEFAULT_PUSH_URL = 'https://push.opinum.com'


class ApiConnector:
    time_limit = 3 * 60  # Three minutes

    def __init__(self,
                 environment=None,
                 account_id=None):
        self.environment = os.environ if environment is None else environment
        self.api_url = self.environment.get('API_URL', DEFAULT_API_URL)
        self.auth_url = self.environment.get('AUTH_URL', DEFAULT_AUTH_URL)
        self.push_url = f"{self.environment.get('PUSH_URL', DEFAULT_PUSH_URL)}/api/data/"
        self.scope = self.environment.get('SCOPE', DEFAULT_SCOPE)
        self.account_id = account_id
        self.creation_time = None
        self.token = None
        self.set_token()

    def set_token(self):
        oauth = OAuth2Session(client=LegacyApplicationClient(client_id=self.environment['OPISENSE_CLIENT_ID']))
        args = {
            'token_url': f"{self.auth_url}/connect/token",
            'scope': self.scope,
            'username': self.environment['OPISENSE_USERNAME'],
            'password': self.environment['OPISENSE_PASSWORD'],
            'client_id': self.environment['OPISENSE_CLIENT_ID'],
            'client_secret': self.environment['OPISENSE_SECRET'],
            'auth': None
        }
        if self.account_id is not None:
            args['acr_values'] = f"accountId:{self.account_id}"
        self.token = oauth.fetch_token(**args)
        self.creation_time = dt.datetime.now()

    @property
    def headers(self):
        if (dt.datetime.now() - self.creation_time).total_seconds() > self.time_limit:
            self.set_token()
        return {"Content-Type": "application/json",
                "Authorization": f"Bearer {self.token['access_token']}"}

    def _process_request(self, method, url, data, **kwargs):
        if data is not None:
            data = json.dumps(data)
        params = dict()
        for k, v in kwargs.items():
            if isinstance(v, dt.datetime):
                v = v.strftime('%Y-%m-%dT%H:%M:%S')
            if k == 'date_from':
                k = 'from'
            params[k] = v

        response = method(url, data=data, params=params, headers=self.headers)
        return response

    def get(self, endpoint, data=None, **kwargs):
        return self._process_request(requests.get,
                                     f"{self.api_url}/{endpoint}",
                                     data,
                                     **kwargs)

    def post(self, endpoint, data=None, **kwargs):
        return self._process_request(requests.post,
                                     f"{self.api_url}/{endpoint}",
                                     data,
                                     **kwargs)

    def put(self, endpoint, data=None, **kwargs):
        return self._process_request(requests.put,
                                     f"{self.api_url}/{endpoint}",
                                     data,
                                     **kwargs)

    def delete(self, endpoint, data=None, **kwargs):
        return self._process_request(requests.delete,
                                     f"{self.api_url}/{endpoint}",
                                     data,
                                     **kwargs)

    def push_data(self, df, **kwargs):
        kwargs['data'] = df.to_dict('records')
        return self._process_request(requests.post,
                                     self.push_url,
                                     [kwargs])


