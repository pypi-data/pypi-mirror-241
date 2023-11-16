import os
from oauthlib.oauth2 import LegacyApplicationClient
from requests_oauthlib import OAuth2Session
import json
import requests
import datetime as dt
import logging
from time import sleep

DEFAULT_API_URL = 'https://api.opinum.com'
DEFAULT_AUTH_URL = 'https://identity.opinum.com'
DEFAULT_SCOPE = 'opisense-api'
DEFAULT_PUSH_URL = 'https://push.opinum.com'


class ApiConnector:
    """
    A class for connection to Opinum API

    :param environment: a dictionary with all environment variables
    :param account_id: the account id to use (for users having access to multiple tenants)
    :param retries_when_connection_failure: allows to make several attempts to have a successful query (connection issues can happen)
    """

    time_limit = 3 * 60  # Three minutes

    MAX_RETRIES_WHEN_CONNECTION_FAILURE = 5

    def __init__(self,
                 environment=None,
                 account_id=None,
                 retries_when_connection_failure=0,
                 seconds_between_retries=5):
        self.environment = os.environ if environment is None else environment
        self.api_url = self.environment.get('OPINUM_API_URL', DEFAULT_API_URL)
        self.auth_url = self.environment.get('OPINUM_AUTH_URL', DEFAULT_AUTH_URL)
        self.push_url = f"{self.environment.get('OPINUM_PUSH_URL', DEFAULT_PUSH_URL)}/api/data/"
        self.scope = self.environment.get('OPINUM_SCOPE', DEFAULT_SCOPE)
        self.account_id = account_id
        self.creation_time = None
        self.token = None
        self._set_token()
        self.max_call_attempts = 1 + min(retries_when_connection_failure, self.MAX_RETRIES_WHEN_CONNECTION_FAILURE)
        self.seconds_between_retries = seconds_between_retries

    def _set_token(self):
        oauth = OAuth2Session(client=LegacyApplicationClient(client_id=self.environment['OPINUM_CLIENT_ID']))
        args = {
            'token_url': f"{self.auth_url}/connect/token",
            'scope': self.scope,
            'username': self.environment['OPINUM_USERNAME'],
            'password': self.environment['OPINUM_PASSWORD'],
            'client_id': self.environment['OPINUM_CLIENT_ID'],
            'client_secret': self.environment['OPINUM_SECRET'],
            'auth': None
        }
        if self.account_id is not None:
            args['acr_values'] = f"accountId:{self.account_id}"
        self.token = oauth.fetch_token(**args)
        self.creation_time = dt.datetime.now()

    @property
    def _headers(self):
        if (dt.datetime.now() - self.creation_time).total_seconds() > self.time_limit:
            self._set_token()
        return {"Content-Type": "application/json",
                "Authorization": f"Bearer {self.token['access_token']}"}

    def _process_request(self, method, url, data, **kwargs):
        attempts = 0
        while attempts < self.max_call_attempts:
            try:
                if data is not None:
                    data = json.dumps(data)
                params = dict()
                for k, v in kwargs.items():
                    if isinstance(v, dt.datetime):
                        v = v.strftime('%Y-%m-%dT%H:%M:%S')
                    if k == 'date_from':
                        k = 'from'
                    params[k] = v

                response = method(url, data=data, params=params, headers=self._headers)
                assert response.status_code in (200, 204)
                return response
            except (requests.exceptions.ConnectionError, AssertionError) as error:
                attempts += 1
                logging.warning(f"Failure {attempts}")
                sleep(self.seconds_between_retries)
        if attempts == self.max_call_attempts:
            logging.error(error)
            raise error

    def get(self, endpoint, **kwargs):
        """
        Method for data query in the API

        :param endpoint: the Opinum API endpoint
        :param kwargs: dictionary of API call parameters
        :return: the http request response
        """

        return self._process_request(requests.get,
                                     f"{self.api_url}/{endpoint}",
                                     data=None,
                                     **kwargs)

    def post(self, endpoint, data=None, **kwargs):
        """
        Method for data creation in the API

        :param endpoint: the Opinum API endpoint
        :param data: body of the request
        :param kwargs: dictionary of API call parameters
        :return: the http request response
        """
        return self._process_request(requests.post,
                                     f"{self.api_url}/{endpoint}",
                                     data,
                                     **kwargs)

    def put(self, endpoint, data=None, **kwargs):
        """
        Method for data update in the API

        :param endpoint: the Opinum API endpoint
        :param data: body of the request
        :param kwargs: dictionary of API call parameters
        :return: the http request response
        """
        return self._process_request(requests.put,
                                     f"{self.api_url}/{endpoint}",
                                     data,
                                     **kwargs)

    def delete(self, endpoint, data=None, **kwargs):
        """
        Method for data deletion in the API

        :param endpoint: the Opinum API endpoint
        :param data: body of the request
        :param kwargs: dictionary of API call parameters
        :return: the http request response
        """
        return self._process_request(requests.delete,
                                     f"{self.api_url}/{endpoint}",
                                     data,
                                     **kwargs)

    def push_data(self, body):
        """
        Method for data push in the API

        :param body: see https://docs.opinum.com/articles/push-formats/standard-format.html
        :return: the http request response
        """
        return self._process_request(requests.post,
                                     self.push_url,
                                     body)

    def push_dataframe_data(self, df, **kwargs):
        """
        Method for data push in the API using a pandas DataFrame

        :param df: a pandas dataframe with dates in ISO format in 'date' column and values in 'value' column
        :param kwargs: dictionary of API call parameters, allowing to identify the target variable (see https://docs.opinum.com/articles/push-formats/standard-format.html)
        :return: the http request response
        """
        kwargs['data'] = df.to_dict('records')
        return self.push_data([kwargs])


