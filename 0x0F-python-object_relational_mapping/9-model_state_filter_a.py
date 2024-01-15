#!/usr/bin/python3
"""
    A script that lists all State objects that contain
    the letter a from the database
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    """ Query State objects where name starts with A """
    state = session.query(State).filter(State.name.like('B%')).all()
    print(state.id, state.name, sep=": ")
