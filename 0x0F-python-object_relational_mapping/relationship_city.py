#!/usr/bin/python3

"""
Module defining the City class for SQLAlchemy.

This module contains the definition of the City class,
which represents a city in a database.
"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
    Class representing a city in the database.

    Args:
        __tablename__ (str): The name of the MySQL table to store cities.
        id (sqlalchemy.Integer): The city's id.
        name (sqlalchemy.String): The city's name.
        state_id (sqlalchemy.Integer): The foreign key referencing the id of
        the associated state.
    """

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
