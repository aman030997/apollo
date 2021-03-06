from pathlib import Path

from django.test import TestCase, Client

TEST_DIR = Path(__file__).parent / Path('test_files')


# this case seems incorrect. there's no addresses field in address.xml yet it is expected in test case.
# also, root is expected in first test case while ignored in second.
class XMLConversionTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.maxDiff = None

    def test_convert_empty_document(self):
        with (TEST_DIR / Path('empty.xml')).open() as fp:
            response = self.client.post('/', {
                'file': fp,
            })
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json(), {
                "Root": "",
            })

    def test_convert_addresses(self):
        with (TEST_DIR / Path('addresses.xml')).open() as fp:
            response = self.client.post('/', {
                'file': fp,
            })
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json(), {
                "Addresses": [
                    {
                        "Address": [
                            {"StreetLine1": "123 Main St."},
                            {"StreetLine2": "Suite 400"},
                            {"City": "San Francisco"},
                            {"State": "CA"},
                            {"PostCode": "94103"},
                        ]
                    },
                    {
                        "Address": [
                            {"StreetLine1": "400 Market St."},
                            {"City": "San Francisco"},
                            {"State": "CA"},
                            {"PostCode": "94108"},
                        ]
                    },
                ],
            })
