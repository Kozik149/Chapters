from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date

engine = create_engine('sqlite:///sky.db', echo=False)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Tasks(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    deadline = Column(Date)
    description = Column(String)
    task_hash = Column(String)


Base.metadata.create_all(engine)
