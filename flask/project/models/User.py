from project import Base
from sqlalchemy import Column, Integer, Boolean, String
from sqlalchemy.types import DateTime

# Tasks table
class User(Base):
    __tablename__ = 'users'
    __table_args__ = { 'schema':'private' , 'extend_existing': True}
    id = Column(Integer, primary_key=True)
    username = Column(String(25))
    email = Column(String(35))
    password = Column(String(256))
    date_joined = Column(DateTime())
