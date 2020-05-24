from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from Database_connection.DBconnection import DBconnection
from model.ORMbase import Base


class ProductCategory(Base):
    __tablename__ = 'product_category'
    cat_id = Column(Integer, primary_key=True)
    catname = Column(String)
    ProductObject = relationship("Product", back_populates="ProductCategoryObject")

    def get_product_category(self):
        db = DBconnection()
        session = db.getConnection_parameters()
        catId = self.cat_id
        productCategory = session.query(ProductCategory).get(catId)
        session.close()
        return productCategory

    def add_product_category(self):
        db = DBconnection()
        session = db.getConnection_parameters()
        session.add(self)
        session.commit()
        session.close()

    def delete_product_category(self):
        categoryId = self.cat_id
        db = DBconnection()
        session = db.getConnection_parameters()
        session.query(ProductCategory).filter(ProductCategory.cat_id == categoryId).delete()
        session.commit()
        session.close()

    def update_product_category(self):
        categoryId = self.cat_id
        db = DBconnection()
        session = db.getConnection_parameters()
        existing_productCategory = session.query(ProductCategory).get(categoryId)
        existing_productCategory.catname = self.catname
        session.commit()
        session.close()


def get_all_product_category():
    db = DBconnection()
    session = db.getConnection_parameters()
    productCategoryList = session.query(ProductCategory).all()
    session.close()
    return productCategoryList
