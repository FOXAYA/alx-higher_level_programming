#!/usr/bin/python3
"""Script creates State California and City San Francisco in database
Takes three arguments
    mysql username
    mysql password
    database name
Connects to host localhost and default port (3306)
"""
if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from relationship_state import Base, State
    from relationship_city import City
    from sys import argv
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    session = Session(bind=engine)
    ca = State(name="California", cities=[City(name="San Francisco")])
    session.add(ca)
    session.commit()
    session.close()
