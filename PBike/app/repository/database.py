import threading

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from app.core.QueryEntity import QueryEntity

#  add reference to register automatic creation


from app.core.BikeEntity import BikeEntity


engine = create_engine('sqlite:///manual.db')
QueryEntity.metadata.create_all(bind=engine)


db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

QueryEntity.query = db_session.query_property()


def db_init():
    QueryEntity.metadata.create_all(bind=engine)
