from sqlalchemy import Column, String, Table, Integer, Date
from sqlalchemy.ext.declarative import declarative_base
from Database_connection.DBconnection import DBconnection

Base = declarative_base()


class Customer(Base):
    __tablename__ = 'customer'
    cid = Column(Integer, primary_key=True)
    firstname = Column(String)
    surname = Column(String)
    email = Column(String)
    password = Column(String)
    dob = Column(Date)
    mobile_number = Column(String)