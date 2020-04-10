"""
    __init__.py
        - Imports Flask
        - Creates the app callable object
"""
import os
from flask import Flask
from flask_bootstrap import Bootstrap

from sqlalchemy import create_engine, event, DDL
from sqlalchemy.schema import CreateSchema
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)
app.secret_key = os.environ['APP_SECRET_KEY']
bs = Bootstrap(app)




# Same environment variables used inside PostGres db
user = os.environ['POSTGRES_USER']
pwd = os.environ['POSTGRES_PASSWORD']
database = os.environ['POSTGRES_DB']

# Network name set by docker & PostGres default port number
host = 'db'
port = '5432'
engine = create_engine('postgres://%s:%s@%s:%s/%s' % (user, pwd, host, port, database), echo=True)

db_session = scoped_session(sessionmaker(autocommit=False,
    autoflush=False,
    bind=engine))

Base = declarative_base()
Base.query = db_session.query_property


def create_tables():
    # TODO: import modules that define models for cleaner code
    import project.models
    print("~~~Creating Schemas and tables if not made~~~")
    event.listen(Base.metadata, 'before_create', DDL("CREATE SCHEMA IF NOT EXISTS private"))
    event.listen(Base.metadata, 'before_create', DDL("CREATE SCHEMA IF NOT EXISTS public"))
    Base.metadata.create_all(engine)

create_tables()
from project import views
from project import admin_views
