#!/usr/bin/python3
"""
A script that lists all State objects that contain the letter
a from the database hbtn_0e_6_usa

Your script should take 3 arguments: mysql username,
mysql password and database name
You must use the module SQLAlchemy
You must import State and Base from model_state -
from model_state import Base, State
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
The results must be displayed as they are in the example below
Your code should not be executed when imported
"""

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv

if __name__ == "__main__":
    querry = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(
        querry.format(argv[1], argv[2], argv[3])
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for states in session.query(State).filter(State.name.like('%a%')).all():
        print("{}: {}".format(states.id, states.name))
