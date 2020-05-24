from sqlalchemy import Column, String, Integer, ForeignKey
from model.ORMbase import Base
from sqlalchemy.orm import relationship
from Database_connection.DBconnection import DBconnection


class Address(Base):
    __tablename__ = 'address'
    aid = Column(Integer, primary_key=True)
    cid = Column(Integer, ForeignKey("customer.cid"))
    description = Column(String)
    state = Column(String)
    district = Column(String)
    pin_no = Column(String)
    CustomerObject = relationship("Customer", back_populates="AddressObject")

    def add_address(self):
        db = DBconnection()
        session = db.getConnection_parameters()
        session.add(self)
        session.commit()
        session.close()

    def get_address(self):
        db = DBconnection()
        session = db.getConnection_parameters()
        customer_id = self.cid
        result = session.query(Address).filter(Address.cid == customer_id)
        session.close()
        return result

    def update_address(self):
        db = DBconnection()
        session = db.getConnection_parameters()
        addressId = self.aid
        existingAddress = session.query(Address).get(addressId)
        existingAddress.cid = self.cid
        existingAddress.description = self.description
        existingAddress.state = self.state
        existingAddress.district = self.district
        existingAddress.pin_no = self.pin_no
        session.commit()
        session.close()

    def delete_address(self):
        db = DBconnection()
        session = db.getConnection_parameters()
        customer_id = self.cid
        session.query(Address).filter(Address.cid == customer_id).delete()
        session.commit()
        session.close()
