from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from Database_connection.DBconnection import DBconnection
from model.ORMbase import Base


class Product(Base):
    __tablename__ = 'product'
    pid = Column(Integer, primary_key=True)
    catid = Column(Integer, Foreignkey='product_category.cat_id')
    product_name = Column(String)
    quantity = Column(Integer)
    ProductCategoryObject = relationship("ProductCategory", back_populates="ProductObject")
    KartObject = relationship("Kart", back_populates="ProductObject")

    def get_product(self):
        db = DBconnection()
        session = db.getConnection_parameters()
        productId = self.pid
        product = session.query(Product).get(productId)
        session.close()
        return product

    def add_product(self):
        db = DBconnection()
        session = db.getConnection_parameters()
        session.add(self)
        session.commit()
        session.close()

    def update_product(self):
        productId = self.pid
        db = DBconnection()
        session = db.getConnection_parameters()
        existing_product = session.query(Product).get(productId)
        existing_product.catid = self.catid
        existing_product.product_name = self.product_name
        existing_product.quantity = self.quantity
        session.commit()
        session.close()

    def delete_product(self):
        productId = self.pid
        db = DBconnection()
        session = db.getConnection_parameters()
        session.query(Product).filter(Product.pid == productId).delete()
        session.commit()
        session.close()


def get_all_product():
    db = DBconnection()
    session = db.getConnection_parameters()
    productList = session.query(Product).all()
    session.close()
    return productList
