import unittest
from opinum_api_connector import ApiConnector


class MyTestCase(unittest.TestCase):
    def test_instance_creation_with_bad_credentials(self):
        with self.assertRaises(Exception) as context:
            api_connector = ApiConnector(environment={
                'OPISENSE_CLIENT_ID': 'client',
                'OPISENSE_USERNAME': 'user',
                'OPISENSE_PASSWORD': 'password',
                'OPISENSE_SECRET': 'secret'
            })
        self.assertTrue('(invalid_client) ' in str(context.exception))


if __name__ == '__main__':
    unittest.main()
