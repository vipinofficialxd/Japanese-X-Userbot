import os
from sqlalchemy import create_engine, exc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from X import LOGGER

BASE = declarative_base()

def start(db_url) -> scoped_session:
    try:
        engine = create_engine(db_url)
        BASE.metadata.bind = engine
        BASE.metadata.create_all(engine)
        return scoped_session(sessionmaker(bind=engine, autoflush=False))
    except exc.OperationalError as e:
        LOGGER(__name__).warning(
            "Failed to connect to the database. Check your DB_URL configuration."
        )
        LOGGER(__name__).info(str(e))
        return None


DB_AVAILABLE = False

def mulaisql(db_url) -> scoped_session:
    global DB_AVAILABLE
    try:
        engine = create_engine(db_url, client_encoding="utf8")
        BASE.metadata.bind = engine
        BASE.metadata.create_all(engine)
        DB_AVAILABLE = True
        return scoped_session(sessionmaker(bind=engine, autoflush=False))
    except exc.OperationalError:
        DB_AVAILABLE = False
        LOGGER(__name__).warning(
            "Failed to connect to the database. Check your DB_URL configuration."
        )
        return None
