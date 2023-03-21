"""Модели таблиц"""
import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Publisher(Base):
    __tablename__ = "publisher"
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String, unique=True, nullable=False)


class Shop(Base):
    __tablename__ = "shop"
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String, unique=True, nullable=False)


class Book(Base):
    __tablename__ = "book"
    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String, nullable=False)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey("publisher.id"), nullable=False)

    publisher = relationship(Publisher, backref="book")


class Stock(Base):
    __tablename__ = "stock"
    id = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey("book.id"), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey("shop.id"), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)

    book = relationship(Book, backref="stock")
    shop = relationship(Shop, backref="shop")


class Sale(Base):
    __tablename__ = "sale"
    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Float, nullable=False)
    date_sale = sq.Column(sq.Date, nullable=False)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey("stock.id"), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)

    stock = relationship(Stock, backref="sale")



