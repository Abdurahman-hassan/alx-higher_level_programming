#!/usr/bin/python3

"""
Module defining the City class for SQLAlchemy.

This module contains the definition of the City class,
which represents a city in a database.
"""

from sqlalchemy import Column, ForeignKey, Integer, String
from model_state import Base


class City(Base):
    """
    Class representing a city in the database.

    Args:
        id (int): The primary key identifier for the city.
        name (str): The name of the city.
        state_id (int): The foreign key referencing the id of the
        associated state.
    """

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
