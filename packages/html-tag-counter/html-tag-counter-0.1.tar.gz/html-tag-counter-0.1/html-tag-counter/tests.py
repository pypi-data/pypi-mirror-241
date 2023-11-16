import unittest
import functions as fc
import argparse
import mock


class Test(unittest.TestCase):
    def test_add_protocol_to_url(self):
        self.assertEqual(fc.add_protocol_to_url("google.com"), "http://google.com")

    def test_parse_tagcounter_args(self):
        self.assertIsInstance(fc.parse_tagcounter_args(), argparse.Namespace)

    @mock.patch("functions.parse_yaml_file")
    def test_get_synonym(self, parse_mock):
        parse_mock.return_value = {"1": "11", "2": "22"}
        self.assertEqual(fc.get_synonym("1"), "11")
        self.assertEqual(fc.get_synonym(5), 5)


if __name__ == "__main__":
    unittest.main()
