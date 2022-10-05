import datetime
import unittest

from python.helpers.db.db import to_python_datetime


class TestDB(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestDB, self).__init__(*args, **kwargs)
        self.now = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0)

    def test_to_python_datetime(self):
        self.assertIsInstance(
            to_python_datetime(self.now.strftime('%Y-%m-%d %H:%M:%S')),
            datetime.datetime,
            "Bad conversion for format '%Y-%m-%d %H:%M:%S'"
        )

        self.assertIsInstance(
            to_python_datetime(self.now.strftime('%Y-%m-%d %H:%M:%S%z')),
            datetime.datetime,
            "Bad conversion for format '%Y-%m-%d %H:%M:%S%z'"
        )

        self.assertIsInstance(
            to_python_datetime(self.now.strftime('%Y-%m-%dT%H:%M:%S%z')),
            datetime.datetime,
            "Bad conversion for format '%Y-%m-%dT%H:%M:%S%z'"
        )

        self.assertIsInstance(
            to_python_datetime(self.now.isoformat()),
            datetime.datetime,
            "Bad conversion for format '%Y-%m-%d %H:%M:%S'"
        )

    def test_to_python_datetime_raises(self):
        self.assertRaises(
            ValueError,
            to_python_datetime,
            'foobar'
        )

        self.assertRaises(
            TypeError,
            to_python_datetime,
            self.now.timestamp()
        )


if __name__ == "__main__":
    unittest.main()
