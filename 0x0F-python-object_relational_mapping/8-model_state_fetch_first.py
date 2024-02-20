#!/usr/bin/python3
'''Script for Task 8'''

# Import necessary modules and classes
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
import sys

if __name__ == '__main__':
    """ Extract MySQL username, password, and database name from
    command-line arguments """
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    host = 'localhost'
    port = '3306'

    # Create a SQLAlchemy engine to connect to the MySQL database with NullPool
    engine = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'.format(
                           username, password, host, port, db_name),
                           pool_pre_ping=True, poolclass=NullPool)

    # Create a session factory bound to the engine
    Session = sessionmaker(bind=engine)

    # Create a session
    local_session = Session()

    # Query the first State object, ordered by ID
    result = local_session.query(State).order_by(State.id).first()

    # Close the session to release resources
    local_session.close()

    """ Print the ID and name of the first state if
    found, otherwise print 'Nothing'"""
    if result:
        print('{}: {}'.format(result.id, result.name))
    else:
        print('Nothing')
