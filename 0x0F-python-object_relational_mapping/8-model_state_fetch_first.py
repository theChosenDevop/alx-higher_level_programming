#!/usr/bin/python3
""" A script that prints the first State object from the database hbtn_0e_6_usa """
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

    try:
        oneState = session.query(State).first()

        if oneState is None:
            print('Nothing')
        else:
            print(oneState)
    except Exception as e:
        print("Error:", e)

    finally:
        session.close()
