from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship
from Database_connection.DBconnection import DBconnection
from model.ORMbase import Base


class Kart(Base):
    __tablename__ = 'kart'
    kid = Column(Integer, primary_key=True)
    cid = Column(Integer, Foreignkey="customer.cid")
    pid = Column(Integer, Foreignkey="product.pid")
    CustomerObject = relationship("Customer", back_populates="KartObject")
    ProductObject = relationship("Product", back_populates="KartObject")

    def get_kart_product(self):
        db = DBconnection()
        session = db.getConnection_parameters()
        kardId = self.kid
        kartProduct = session.query(Kart).get(kardId)
        session.close()
        return kartProduct

    def add_kart_product(self):
        db = DBconnection()
        session = db.getConnection_parameters()
        session.add(self)
        session.commit()
        session.close()

    def update_kart_product(self):
        kardId = self.kid
        db = DBconnection()
        session = db.getConnection_parameters()
        existing_kart_product = session.query(Kart).get(kardId)
        existing_kart_product.cid = self.cid
        existing_kart_product.pid = self.pid
        session.commit()
        session.close()

    def delete_kart_product(self):
        kardId = self.kid
        db = DBconnection()
        session = db.getConnection_parameters()
        session.query(Kart).filter(Kart.kid == kardId).delete()
        session.commit()
        session.close()


def get_all_kart_product():
    db = DBconnection()
    session = db.getConnection_parameters()
    kartProductList = session.query(Kart).all()
    session.close()
    return kartProductList
