#!/usr/bin/python3
"""Script that adds the State object 'Louisiana'
to the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new State object for Louisiana
    new_state = State(name="Louisiana")
    session.add(new_state)  # Add the new state to the session
    session.commit()  # Commit the transaction to save changes

    # Print the ID of the newly added state
    print("{}".format(new_state.id))

    # Close the session
    session.close()
