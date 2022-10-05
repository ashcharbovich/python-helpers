import psycopg2.extras


def to_postgres_json(value):
    """
    Convert data into json data type
    :param value:
    :return:
    """

    return psycopg2.extras.Json(value)
