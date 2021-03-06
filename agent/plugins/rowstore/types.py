"""
This module provides type-guessing for a providing collection
of rows (which originate either from a CSV or an Excel file).
"""
__copyright__ = "Copyright (C) 2016 University of Maryland"
__license__ = "GNU AFFERO GENERAL PUBLIC LICENSE, Version 3"


import collections
import csv
from cStringIO import StringIO
import operator

from drastic.drivers import get_driver


def is_int(x):
    try:
        int(x)
        return True
    except ValueError:
        return False


def is_float(x):
    try:
        float(x)
        return True
    except ValueError:
        return False


def _update_scores(d, k):
    d["int"] += 0
    d["float"] += 0
    d["timestamp"] += 0
    d["text"] += 0
    d[k] += 1


def is_datetime(x):
    from dateutil.parser import parse
    try:
        parse(x)
        return True
    except ValueError:
        return False


def guess_type(counts):
    """
    Uses the counts to determine the most likely type for each
    column.
    """
    # TODO: Handle multiple results with same value
    # TODO: Work out whether we want most/least specialised
    return max(counts.iteritems(), key=operator.itemgetter(1))[0]


def count_types(resource_url):
    """
    Returns the number of rows processed and a dictionary where
    each key is the column name, and for each type (text,
    int, timestamp) returns the number of times it appearead
    in the reader.

    resource_url should point to a CSV/XLS file.
    """
    rows = 0
    types = collections.defaultdict(lambda: collections.defaultdict(int))

    driver = get_driver(resource_url)
    buff = StringIO()
    for chunk in driver.chunk_content():
        buff.write(chunk)

    reader = csv.DictReader(buff.getvalue().split('\n'))
    for row in reader:
        for k, v in row.iteritems():
            if is_int(v):
                _update_scores(types[k], "int")
            elif is_float(v):
                _update_scores(types[k], "float")
            elif is_datetime(v):
                _update_scores(types[k], "timestamp")
            else:
                _update_scores(types[k], "text")

        rows += 1

    buff.close()
    return rows, types
