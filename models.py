# coding: utf-8
from typing import Annotated

from fastapi import Depends
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import relationship, sessionmaker, Session
from sqlalchemy.orm import declarative_base

Base = declarative_base()
metadata = Base.metadata

engine = create_engine('mysql+mysqlconnector://root:@localhost/e_store_example')
session = sessionmaker(autoflush=False, autocommit=False, bind=engine)


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False, unique=True)


class Customer(Base):
    __tablename__ = 'customer'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False)


class OrderState(Base):
    __tablename__ = 'order_state'

    id = Column(Integer, primary_key=True)
    state = Column(String(45), nullable=False, unique=True)


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(45), nullable=False, unique=True)
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False)


class Order(Base):
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True)
    date_created = Column(DateTime, nullable=False)
    order_state_id = Column(ForeignKey('order_state.id'), nullable=False, index=True)
    customer_id = Column(ForeignKey('customer.id'), nullable=False, index=True)
    handler_id = Column(ForeignKey('user.id'), nullable=False, index=True)

    customer = relationship('Customer')
    handler = relationship('User')
    order_state = relationship('OrderState')


class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    price = Column(Float, nullable=False)
    category_id = Column(ForeignKey('category.id'), nullable=False, index=True)

    category = relationship('Category')


class Boat(Product):
    __tablename__ = 'boat'

    product_id = Column(ForeignKey('product.id'), primary_key=True)
    width_cm = Column(Float, nullable=False)
    length_cm = Column(Float, nullable=False)

    product = relationship('Product')


class Hat(Product):
    __tablename__ = 'hat'

    product_id = Column(ForeignKey('product.id'), primary_key=True)
    color = Column(String(45), nullable=False)
    size = Column(String(45), nullable=False)

    product = relationship('Product')


class Shoe(Product):
    __tablename__ = 'shoe'

    product_id = Column(ForeignKey('product.id'), primary_key=True)
    size = Column(String(45), nullable=False)
    color = Column(String(45), nullable=False)

    product = relationship('Product')


class OrderHasProduct(Base):
    __tablename__ = 'order_has_product'

    order_id = Column(ForeignKey('order.id'), primary_key=True, nullable=False, index=True)
    product_id = Column(ForeignKey('product.id'), primary_key=True, nullable=False, index=True)
    product_count = Column(Integer, nullable=False)

    order = relationship('Order')
    product = relationship('Product')


def init_db():
    try:
        db = session()
        yield db
    finally:
        db.close()


Db = Annotated[Session,Depends(init_db)]
