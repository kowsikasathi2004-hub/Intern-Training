from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column,Integer,String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine( "postgresql://postgres:admin123@localhost:5432/data_db")
print("Database Connection Successful")