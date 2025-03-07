#!/usr/bin/python3
"""Script that prints all City objects
from the database hbtn_0e_14_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to fetch all City objects, sorted by cities.id
    cities = session.query(State.name, City.id, City.name).join(City).\
        order_by(City.id).all()

    # Display results
    for state_name, city_id, city_name in cities:
        print("{}: ({}) {}".format(state_name, city_id, city_name))

    # Close the session
    session.close()
