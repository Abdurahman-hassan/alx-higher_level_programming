#!/usr/bin/python3

"""
Script to query a MySQL database and print the ID of the State object
with the name passed as an argument.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create a connection to the MySQL database using the provided credentials
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    # Create the database schema
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(engine)
    session = Session()

    state_name = sys.argv[4]
    state = session.query(State).filter(State.name == state_name).first()

    if state is None:
        print('Not found')
    else:
        print("{}".format(state.id))
    session.close()
