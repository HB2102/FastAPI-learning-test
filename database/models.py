from database.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class DbUser(Base):
    __tablename__ = 'users'
    id = Column(Integer, index=True, primary_key=True)
    username = Column(String(100))
    password = Column(String(100))
    email = Column(String(100))