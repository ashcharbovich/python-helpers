from dateutil.parser import parse


def to_python_datetime(value):
    """
    Convert data as string into datetime
    :param value:
        A string containing a date/time stamp.
    :return:
        Returns a :class:`datetime.datetime` object
    :raises:
        Raised for invalid or unknown string formats
    """

    return parse(value)
