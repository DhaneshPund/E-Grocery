from sqlalchemy import Column, String, Integer, Date
from model.Address import Address
from model.ORMbase import Base
from sqlalchemy.orm import relationship
from Database_connection.DBconnection import DBconnection


class Customer(Base):
    __tablename__ = 'customer'
    cid = Column(Integer, primary_key=True)
    firstname = Column(String)
    surname = Column(String)
    email = Column(String)
    password = Column(String)
    dob = Column(Date)
    mobile_number = Column(String)
    AddressObject = relationship("Address", back_populates='CustomerObject')

    def get_customer(self):
        db = DBconnection()
        session = db.getConnection_parameters()
        customer_id = self.cid
        fetchedCustomer = session.query(Customer).get(customer_id)
        session.close()
        return fetchedCustomer

    def add_customer(self):
        db = DBconnection()
        session = db.getConnection_parameters()
        session.add(self)
        session.commit()
        session.close()

    def update_customer(self):
        db = DBconnection()
        session = db.getConnection_parameters()
        customerId = self.cid
        existingCustomer = session.query(Customer).get(customerId)
        existingCustomer.firstname = self.firstname
        existingCustomer.surname = self.surname
        existingCustomer.email = self.email
        existingCustomer.password = self.password
        existingCustomer.dob = self.dob
        existingCustomer.mobile_number = self.mobile_number
        session.commit()
        session.close()

    def delete_customer(self):
        customerId = self.cid
        address=Address(cid=customerId)
        address.delete_address()
        db = DBconnection()
        session = db.getConnection_parameters()
        existingCustomer = session.query(Customer).get(customerId)
        session.delete(existingCustomer)
        session.commit()
        session.close()


def get_all_customers():
    db = DBconnection()
    session = db.getConnection_parameters()
    customer_list = session.query(Customer).all()
    session.close()
    return customer_list
