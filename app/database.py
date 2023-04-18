from functools import wraps

import psycopg2

import settings as sett


class DB():
    """ The class is contains methods to connect with DataBase """

    def __init__(self):
        """ Initialization of class object. """
        self.table_name = 'images'
        self._create_table_if_not_exists()

    def _connect(function):
        """ Decorator. get connection and add coursor in function params """

        @wraps(function)
        def wrapper(self, *args, **kwargs):
            """ Wrapper of called function. """
            try:
                connection = psycopg2.connect(**sett.DB_CONNECT_DATA)
                connection.autocommit = True

                with connection.cursor() as cursor:

                    return function(self, cursor, *args, **kwargs)

                connection.close()

            except Exception as e:
                print(e)

        return wrapper

    @_connect
    def insert_values_in_table(self, cursor, weight: int):
        """ Insert data in DB table """
        assert isinstance(weight, int), 'Weight is not int type.'

        cursor.execute(
            f"""
            INSERT INTO {self.table_name} (weight) VALUES ({weight});
            """
        )

    @_connect
    def _create_table_if_not_exists(self, cursor):
        """ Create a new table in database if it not exists. """
        cursor.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {self.table_name}(
                id serial PRIMARY KEY,
                weight integer,
                date timestamp NOT NULL default CURRENT_TIMESTAMP
            );
            """
        )
