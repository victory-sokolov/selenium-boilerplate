from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
db = "mydatabase"

class User(Base):
    __tablename__ = "User"

    id = Column('id', Integer, primary_key=True)
    username = Column('username', String)
    password = Column('password', String)

engine = create_engine(f'sqlite3:///:memory:{db}', echo = True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
