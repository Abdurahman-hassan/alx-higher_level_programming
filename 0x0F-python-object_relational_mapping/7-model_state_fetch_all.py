#!/usr/bin/python3

"""
This script connects to a MySQL database and prints information about
all states from the 'states' table using SQLAlchemy.

Usage: ./script_name.py mysql_username mysql_password database_name
"""

import sys

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

from model_state import Base, State

if __name__ == "__main__":
    # Create a connection to the MySQL database using the provided credentials
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    # Create the database schema
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(engine)
    session = Session()

    # Fetch all states from the database and print their information
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    session.close()
