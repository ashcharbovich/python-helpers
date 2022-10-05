import psycopg2.extras
import unittest

from python.helpers.db.postgres import to_postgres_json


class TestPostgres(unittest.TestCase):

    def test_to_postgres_json(self):
        self.assertIsInstance(
            to_postgres_json({}),
            psycopg2.extras.Json
        )

        self.assertIsInstance(
            to_postgres_json({'foo': 'bar'}).adapted,
            dict
        )

        self.assertIsInstance(
            to_postgres_json(['foo', 'bar']).adapted,
            list
        )

        self.assertIsInstance(
            to_postgres_json('foobar').adapted,
            str
        )


if __name__ == "__main__":
    unittest.main()
