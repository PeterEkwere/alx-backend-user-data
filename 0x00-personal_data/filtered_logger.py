#!/usr/bin/env python3
"""
    This Module contains a function returns message obfuscated
    Author: Peter Ekwere
"""
import re
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
    return re.sub(
        fr'((?:^|\{separator})({"|".join(fields)})=)[^;]*',
        fr'\1{redaction}', message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields):
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        message = record.msg
        new_message = filter_datum(self.fields, self.REDACTION,
                                   message, self.SEPARATOR)
        record.msg = new_message
        return super().format(record)
