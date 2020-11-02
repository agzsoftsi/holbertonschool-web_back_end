#!/usr/bin/env python3
''' 0. Regex-ing: filter_datum
    1. Log formatter: class RedactingFormatter
    2. Create logger
    3. Connect to secure database
    4. Read and filter data
'''

import re
from typing import List
import logging
import mysql.connector
from os import getenv


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    ''' Description: Regex-ing - Write a function called filter_datum that
                     returns the log message obfuscated:

        Arguments:
            fields: a list of strings representing all fields to obfuscate
            redaction: a string representing by what the field will be
                       obfuscated
            message: a string representing the log line
            separator: a string representing by which character is
                           separating all fields in the log line (message)
        The function should use a regex to replace occurrences of certain
        field values.
        filter_datum should be less than 5 lines long and use re.sub to
        perform the substitution with a single regex.
    '''

    for i in fields:
        message = re.sub(i + "=.*?" + separator,
                         i + "=" + redaction + separator,
                         message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        Description: Update the class to accept a list of strings fields
                     constructor argument.

        Implement the format method to filter values in incoming log records
        using filter_datum. Values for fields in fields should be filtered.

        DO NOT extrapolate FORMAT manually. The format method should be less
        than 5 lines long
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ Constructor Method """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Filters values in incoming log records using filter_datum """
        return filter_datum(self.fields, self.REDACTION,
                            super(RedactingFormatter, self).format(record),
                            self.SEPARATOR)


def get_logger() -> logging.Logger:
    ''' Description: Implement a get_logger function that takes no arguments
                     and returns a logging.Logger object.

        The logger should be named "user_data" and only log up to logging.INFO
        level. It should not propagate messages to other loggers. It should
        have a StreamHandler with RedactingFormatter as formatter.

        Create a tuple PII_FIELDS constant at the root of the module containing
        the fields from user_data.csv that are considered PII. PII_FIELDS can
        contain only 5 fields - choose the right list of fields that can are
        considered as "important" PIIs or information that you must hide in
        your logs. Use it to parameterize the formatter.
    '''
    log = logging.getLogger('user_data')
    log.setLevel(logging.INFO)
    log.propagate = False

    sh = logging.StreamHandler()
    formatter = RedactingFormatter(PII_FIELDS)
    sh.setFormatter(formatter)
    log.addHandler(sh)

    return log


def get_db() -> mysql.connector.connection.MySQLConnection:
    ''' Description: you will connect to a secure holberton database to read a
                     users table. The database is protected by a username and
                     password that are set as environment variables on the
                     server named PERSONAL_DATA_DB_USERNAME (set the default as
                     "root"), PERSONAL_DATA_DB_PASSWORD (set the default as an
                     empty string) and PERSONAL_DATA_DB_HOST (set the default
                     as "localhost").

        The database name is stored in PERSONAL_DATA_DB_NAME.

        Implement a get_db function that returns a connector to the database
        (mysql.connector.connection.MySQLConnection object).

           - Use the os module to obtain credentials from the environment
           - Use the module mysql-connector-python to connect to the MySQL
             database (pip3 install mysql-connector-python)
    '''
    connection_db = mysql.connector.connection.MySQLConnection(
        user=getenv('PERSONAL_DATA_DB_USERNAME', 'root'),
        password=getenv('PERSONAL_DATA_DB_PASSWORD', ''),
        host=getenv('PERSONAL_DATA_DB_HOST', 'localhost'),
        database=getenv('PERSONAL_DATA_DB_NAME'))

    return connection_db


def main():
    '''
        Description: Implement a main function that takes no arguments and
                     returns nothing.

        The function will obtain a database connection using get_db and
        retrieve all rows in the users table and display each row under a
        filtered format

        Filtered fields:
                          name
                          email
                          phone
                          ssn
                          password
    '''
    database = get_db()
    cursor = database.cursor()
    cursor.execute("SELECT * FROM users;")
    fields = [i[0] for i in cursor.description]

    log = get_logger()

    for row in cursor:
        str_row = ''.join(f'{f}={str(r)}; ' for r, f in zip(row, fields))
        log.info(str_row.strip())

    cursor.close()
    database.close()


if __name__ == '__main__':
    main()
