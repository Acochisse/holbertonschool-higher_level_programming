#!/usr/bin/python3
"""
Module that deletes a record
""""


def connectToDB():
    """
    connects to DB here:
    """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(State).filter(State.id == 2)\
           .update({State.name: 'New Mexico'})

    session.commit()
    session.close()

if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import update
    connectToDB()
