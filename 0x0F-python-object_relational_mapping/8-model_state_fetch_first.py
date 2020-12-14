#!/usr/bin/python3
"""
Module that lists all State objects in the database
"""


def connectToDB():
    """connects to database"""
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]),
        pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).order_by(State.id).first()
    if state:
        print("{}: {}".format(state.id, state.id))
    else:
        print("Nothing")

    session.close()

if __name__ == '__main__':
    import sys
    from model_state import Base, State
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker
    connectToDB()
