from sqlalchemy import Column, Integer, Date, String
from sqlalchemy.orm import relationship
from Database_connection.DBconnection import DBconnection
from model.ORMbase import Base


class CustomerOrder(Base):
    __tablename__='customer_order'
    oid = Column(Integer, primary_key=True)
    cid = Column(Integer, Foreignkey="customer.cid")
    pid = Column(Integer, Foreignkey="product.pid")
    order_date = Column(Date)
    status = Column(String)
    CustomerObject = relationship("Customer", back_populates="CustomerOrderObject")
    ProductObject = relationship("Product", back_populates="CustomerOrderObject")

    def get_customer_order(self):
        db = DBconnection()
        session = db.getConnection_parameters()
        customerOrderId = self.oid
        customerOrder = session.query(CustomerOrder).get(customerOrderId)
        session.close()
        return customerOrder

    def add_customer_order(self):
        db = DBconnection()
        session = db.getConnection_parameters()
        session.add(self)
        session.commit()
        session.close()

    def update_customer_order(self):
        customerOrderId = self.oid
        db = DBconnection()
        session = db.getConnection_parameters()
        existing_customer_order = session.query(CustomerOrder).get(customerOrderId)
        existing_customer_order.cid = self.cid
        existing_customer_order.pid = self.pid
        existing_customer_order.order_date = self.order_date
        existing_customer_order.status = self.status
        session.commit()
        session.close()

    def delete_customer_order(self):
        customerOrderId = self.oid
        db = DBconnection()
        session = db.getConnection_parameters()
        session.query(CustomerOrder).filter(CustomerOrder.oid == customerOrderId).delete()
        session.commit()
        session.close()


def get_all_customer_order():
    db = DBconnection()
    session = db.getConnection_parameters()
    productList = session.query(CustomerOrder).all()
    session.close()
    return productList
