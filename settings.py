import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_FILE = "agenda.db"
DB_PATH = os.path.dirname(os.path.abspath(__file__))
engine = create_engine(f'sqlite:///{DB_PATH}/{DB_FILE}')



Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

