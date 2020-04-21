from project import Base
from sqlalchemy import Column, Integer, Boolean, String
from sqlalchemy.types import DateTime

# Tasks table
class Tasks(Base):
    __tablename__ = 'tasks'
    __table_args__ = { 'schema':'private' , 'extend_existing': True}
    id = Column(Integer, primary_key=True)
    subject = Column(String(256))
    description = Column(String(1024))
    assigned_to = Column(String(256))
    status = Column(Boolean, default=False)
    date_created = Column(DateTime())
