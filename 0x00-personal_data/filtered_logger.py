#!/usr/bin/env python3
"""
    This Module contains a function returns message obfuscated
    Author: Peter Ekwere
"""
import re
import os
import mysql.connector
from mysql.connector.connection import MySQLConnection
from typing import List
import logging


def filter_datum(fields: List[str], redaction: str,
                 message: List, separator: str) -> str:
    """ This function uses regex to replace occurrences of certain field values

    Args:
        fields (list): a list of strings representing all fields to obfuscate
        redaction (str): a string representing to be obfuscated
        message (list):  a list string representing the log line
        seperator (str): string character separating all fields
    """
    pattern = r'({})([^{}]*)'.format("|".join(fields), separator)
    return re.sub(pattern, fr'\1={redaction}', message)


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """ This method filters values in incoming log records

        Args:
            record (logging.LogRecord): record

        Returns:
            str: _description_
        """
        message = record.getMessage()
        new_message = filter_datum(self.fields, self.REDACTION,
                                   message, self.SEPARATOR)
        record.msg = new_message
        return super().format(record)


def get_logger() -> logging.Logger:
    """This method returns a logger instance

    Returns:
        logging.Logger: _description_
    """
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    formatter = RedactingFormatter(list(PII_FIELDS))
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)
    return logger


def get_db() -> MySQLConnection:
    """ This function returns a connector to the database

    Returns:
        MySQLConnection: _description_
    """
    conn = mysql.connector.connect(
        host=os.getenv('PERSONAL_DATA_DB_HOST'),
        user=os.getenv('PERSONAL_DATA_DB_USERNAME', 'root'),
        password=os.getenv('PERSONAL_DATA_DB_PASSWORD', ''),
        database=os.getenv('PERSONAL_DATA_DB_NAME')
    )
    return conn
