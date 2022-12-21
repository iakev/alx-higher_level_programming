#!/usr/bin/python3
"""
Module that conatains a definition of a State and its
relational mapping using SQLAlchemy
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Class that actually maps the tables in
    MySQL with OOP terminologies and
    """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
