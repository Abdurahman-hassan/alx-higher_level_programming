#!/usr/bin/python3

"""
Script to fetch and print data from the database using SQLAlchemy.

This script connects to a MySQL database and fetches data from the
State and City tables. It then prints the name of each state followed
by the names and IDs of the cities associated with that state.
"""

import sys
from model_state import Base, State
from model_city import City
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

    fetched_data = session.query(State, City). \
        filter(State.id == City.state_id).order_by(City.id).all()

    for state, city in fetched_data:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
