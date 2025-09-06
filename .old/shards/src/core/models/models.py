""" `models/models.py`
    The `models` module contains necessary SQLAlchemy definitions for the database models.
"""

from sqlalchemy                 import  Column, Integer, String, DateTime, JSON
from sqlalchemy.ext.declarative import  declarative_base
import datetime

Base = declarative_base()