from project import Base
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import DateTime
from . import Task

db = SQLAlchemy()

class List(Base):
    __tablename__ = 'lists'
    __table_args__ = { 'schema':'private', 'extend_existing': True }
    id = Column(Integer, primary_key=True)
    name = Column(String(256))
    tasks = relationship('Task', backref='private.lists', lazy=True)

    def add_task(self, subject, description, assigned_to, status):
        t = Tasks(
                subject=subject, 
                descripion=description, 
                assigned_to=assigned_to, 
                status=status, 
                date_created=DateTime(), 
                list_id=self.id
                )
        db.session.add(t)
        db.session.commit()

    def __repr__(self):
        return repr(self.name)
