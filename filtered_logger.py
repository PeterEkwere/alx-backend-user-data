#!/usr/bin/env python3
"""
    This Module contains a function returns message obfuscated
    Author: Peter Ekwere
"""
import re


def filter_datum(fields, redaction, message, separator):
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
