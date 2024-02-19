#!/usr/bin/python3

"""
Module defining the State class for SQLAlchemy.

This module contains the definition of the State class,
which represents a state in a database.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import Base


class State(Base):
    """
    Class representing a state in the database.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store states.
        id (sqlalchemy.Integer): The state's id.
        name (sqlalchemy.String): The state's name.
        cities (sqlalchemy.orm.relationship): The relationship representing the
        state-city association.
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")
