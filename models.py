from sqlalchemy import Column, Integer, String, Boolean, DateTime, INTEGER, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Persons(Base):
    __tablename__ = 'persons'
    rollnumber = Column(String, primary_key=True)
    fullname = Column(String, primary_key=False)
    age = Column(String, primary_key=False)
    profession = Column(String, primary_key=False)

class Addresses(Base):
    __tablename__ = 'addresses'
    id = Column(String, primary_key=True)
    street = Column(String, primary_key=False)
    city = Column(String, primary_key=False)
    state = Column(String, primary_key=False)
    country = Column(String, primary_key=False)
    postal_code = Column(String, primary_key=False)
    created_at = Column(DateTime, primary_key=False)
    updated_at = Column(DateTime, primary_key=False)

