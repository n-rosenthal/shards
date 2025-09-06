""" `models.docid.py`
    Parametric generation of unique identifiers for storable objects.
"""

import datetime;

def docid():
    """
        Generate a unique identifier in the form YYYYMMDDHHMMSSFFF format.
    """
    return datetime.datetime.now().strftime('%Y%m%d%H%M%S%f');