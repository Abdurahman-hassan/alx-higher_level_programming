#!/usr/bin/python3

"""
Script to delete all State objects whose names contain the letter 'a'
from a MySQL database.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create a connection to the MySQL database using the provided credentials
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Fetch all states whose names contain the letter 'a' from the database
    st_to_delete = session.query(State).filter(State.name.like('%a%')).all()

    for state in st_to_delete:
        session.delete(state)
    session.commit()

    session.close()
