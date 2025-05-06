from sqlalchemy import create_engine, text
from os import environ
from dotenv import load_dotenv

class Database:
    def __init__(self):
        load_dotenv()

        # obtain database parameters securely as environment variables
        self._MYSQL_USER = environ.get('MYSQL_USER')
        self._MYSQL_PASSWORD = environ.get('MYSQL_PASSWORD')
        self._MYSQL_HOST = environ.get('MYSQL_HOST')
        self._MYSQL_DB = environ.get('MYSQL_DB')

        # set connection string
        self._params = (f"mysql+pymysql://{self._MYSQL_USER}:"
                        f"{self._MYSQL_PASSWORD}@"
                        f"{self._MYSQL_HOST}/"
                        f"{self._MYSQL_DB}?charset=utf8mb4")

    def find_all_mains(self):
        """
                Get all chars flagged as mains
                :return: results of the select query, in list form
                """
        query = (
            "SELECT char_name FROM sos_bot.characters WHERE char_type = 'Main' ORDER BY char_name"
        )

        return self.get_list(self.execute_read(query), 'char_name')

    def create_engine(self):
        """
        create a new engine object upon request, to prevent
        MySQL server from timing out
        :return: SQL alchemy engine object
        """
        # create the query engine
        return create_engine(self._params)

    def execute_read(self, query):
        """
        Send a read query to database engine
        :query: the formatted query string to send
        to database engine
        :return: results of the operation, in list form
        """
        records_list = []

        # open a connection to database, dynamically close
        # it when with block closes
        with self.create_engine().connect() as conn:
            result = conn.execute(text(query))

            # get query results and, line by line,
            # convert to dict entries; add each
            # dict to list
            for row in result.all():
                row_to_dict = row._asdict()
                records_list.append(row_to_dict)

            conn.close()

        return records_list

    def execute_update(self, query):
        """
        Send an update query to database engine
        :query: the formatted query string to send
        to database engine
        :return: int, representing the results of the operation
        """
        # open a connection to database, dynamically close
        # it when with block closes
        with self.create_engine().connect() as conn:
            # get a count of rows affected, to act as
            # indicator of success or failure
            result = conn.execute(text(query)).rowcount
            conn.commit()

            conn.close()

        return result

    def get_list(self, results, field):
        """
        Take in a list of dicts and return a list of strings
        :param results: list of dict entries
        :param field: the desired dict key
        :return: list of dict values corresponding to the given key
        """
        results_list = []

        for result in results:
            results_list.append(result[field])

        return results_list