#!/usr/bin/python3
"""
Module that manages MySQLdb with MySQLAlchemy
"""
import sys
from sqlalchemy import (create_engine)
from model_state import Base, State


class State(base):
    __tablename__ = 'states'

    id = Column(INteger, autoincrement=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
