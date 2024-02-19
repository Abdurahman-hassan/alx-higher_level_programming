#!/usr/bin/python3

"""Defines an ORM class for the 'states' table using SQLAlchemy."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Represents a 'state' entity within a MySQL database using SQLAlchemy.

    Attributes:
        __tablename__ (str): Specifies the table name in the database.
        id (Integer): Defines the primary key column in the table.
        name (String): Holds the name of the state.
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
