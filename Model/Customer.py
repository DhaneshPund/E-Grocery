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

    def add_customer(self):
        db = DBconnection()
        session = db.getConnection_parameters()
        session.add(self)
        session.commit()

    def get_all_customers(self):
        db = DBconnection()
        session = db.getConnection_parameters()
        customer_list = session.query(Customer).all()
        return customer_list

    def update_customer(self):
        db = DBconnection()
        session = db.getConnection_parameters()
        customerId = self.cid
        exstingCustomer = session.query(Customer).get(customerId)
        print(exstingCustomer, "cid: ", customerId)
        exstingCustomer.firstname = self.firstname
        exstingCustomer.surname = self.surname
        exstingCustomer.email = self.email
        exstingCustomer.password = self.password
        exstingCustomer.dob = self.dob
        exstingCustomer.mobile_number = self.mobile_number
        session.commit()

    def delete_customer(self):
        db = DBconnection()
        session = db.getConnection_parameters()
        customerId = self.cid
        exstingCustomer = session.query(Customer).get(customerId)
        session.delete(exstingCustomer)
        session.commit()