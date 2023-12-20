from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql.expression import and_, or_



engine = create_engine("sqlite:///FastAPI.db", connect_args={'check_same_thread':False})
Base = declarative_base()
sessionlocal = sessionmaker(bind=engine, autoflush=False)

def get_db():
    session = sessionlocal()

    try:
        yield session
    finally:
        session.close()

