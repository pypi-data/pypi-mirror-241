import unittest
from opinum_api_connector import ApiConnector
import json
import concurrent.futures

with open('local.settings.json') as f:
    environment = json.load(f)


def get_number_of_sources(connector, source_ids):
    sources = connector.get('sources', ids=source_ids).json()
    return len(sources)


class MyTestCase(unittest.TestCase):
    def test_threads(self):
        api_connector = ApiConnector(environment=environment, account_id=836)
        counter = 0
        futures = list()
        with concurrent.futures.ProcessPoolExecutor(max_workers=10) as executor:
            for first_digits in range(40, 50):
                for mid_digits in range(100):
                    futures.append(executor.submit(get_number_of_sources,
                                                   api_connector,
                                                   [(first_digits * 100 + mid_digits) * 100 + i for i in range(100)]))
                while True:
                    all_finished = True
                    for i, future in enumerate(futures):
                        if future.done():
                            counter += future.result()
                            futures.pop(i)
                        else:
                            all_finished = False
                    if all_finished:
                        break
        self.assertEqual(counter, 31)


if __name__ == '__main__':
    unittest.main()
