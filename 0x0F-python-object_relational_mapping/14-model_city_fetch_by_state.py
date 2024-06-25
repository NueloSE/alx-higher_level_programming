#!/usr/bin/python3

"""
A script 14-model_city_fetch_by_state.py that prints all City objects
from the database hbtn_0e_14_usa:

Your script should take 3 arguments: mysql username,
mysql password and database name
You must use the module SQLAlchemy
You must import State and Base from model_state -
from model_state import Base, State
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by cities.id
Results must be display as they are in the example below
(<state name>: (<city id>) <city name>)
Your code should not be executed when imported
"""

from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    querry = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(
        querry.format(argv[1], argv[2], argv[3])
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state, city in session.query(State, City) \
            .filter(State.id == City.state_id) \
            .order_by(City.id) \
            .all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))
