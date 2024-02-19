#!/usr/bin/python3

"""
Script to add a city to a state in the database using SQLAlchemy.
"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create a connection to the MySQL database using the provided credentials
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    session.add(City(name="San Francisco", state=State(name="California")))
    session.commit()

    session.close()
