import unittest
from st_cockroachdb_connection import util


class UnitTests(unittest.TestCase):
    def test_extract_conn_kwargs(self):
        params = ("url", "dialect", "username", "password")
        target = {"url": "https://www.example.com", "dialect": "postgresql", "username": "postgres",
                  "password": "postgres", "host": "localhost", "port": "26257", "database": "postgres"}
        expected = {'url': 'https://www.example.com', 'dialect': 'postgresql',
                    'username': 'postgres', 'password': 'postgres'}
        self.assertEqual(util.extract_conn_kwargs(params, target), expected)


if __name__ == "__main__":
    unittest.main()
