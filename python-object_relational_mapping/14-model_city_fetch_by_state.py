#!/usr/bin/python3
"""""Lists all states in a database using ORM"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.
        format(username, password, db)
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State, City).filter(
        City.state_id == State.id).order_by(City.id).all()

    for state, city in states:
        print("{}: ({}) {}".format
              (state.name, city.id, city.name))
    session.close()
