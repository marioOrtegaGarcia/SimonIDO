from project import db
from sqlalchemy import Column, Integer, Boolean, String
from sqlalchemy.types import DateTime

# Tasks table
class Tasks(db):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    subject = Column(String(256))
    description = Column(String(1024))
    status = Column(Boolean, unique=False, default=False)
    assigned_to = Column(String(256))
    data_created = Column(DateTime())
