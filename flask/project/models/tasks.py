from project import Base
from sqlalchemy import Column, Integer, Boolean, String
from sqlalchemy.types import DateTime

# Tasks table
class Tasks(Base):
    __tablename__ = 'tasks'
    __table_args__ = { 'schema':'private' }
    id = Column(Integer, primary_key=True)
    subject = Column(String(256))
    description = Column(String(1024))
    status = Column(Boolean, unique=False, default=False)
    assigned_to = Column(String(256))
    data_created = Column(DateTime())
