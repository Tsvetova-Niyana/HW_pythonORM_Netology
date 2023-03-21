import json
import os

from models import Publisher, Shop, Book, Stock, Sale, Base

current = os.getcwd()
folder = "fixtures"
file_name = "tests_data.json"
full_path = os.path.join(current, folder, file_name)


def load_db(session):
    """Функция для загрузки данных в БД"""
    with open(full_path, 'r') as fd:
        data = json.load(fd)

    for record in data:
        model = {
            'publisher': Publisher,
            'shop': Shop,
            'book': Book,
            'stock': Stock,
            'sale': Sale,
        }[record.get('model')]
        session.add(model(id=record.get('pk'), **record.get('fields')))


def create_tables(engine):
    """Функция для создания таблиц в БД"""
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def get_query(session, name_publisher):
    """
    Запрос выборки магазинов, продающих целевого издателя.

    Напишите Python-скрипт, который:

    подключается к БД любого типа на ваш выбор, например, к PostgreSQL;
    импортирует необходимые модели данных;
    принимает имя или идентификатор издателя (publisher), например, через input().
    Выводит построчно факты покупки книг этого издателя:
    название книги | название магазина, в котором была куплена эта книга | стоимость покупки | дата покупки

    """
    check_publisher = session.query(Publisher).filter(Publisher.name == name_publisher).all()
    query = session.query(Book.title, Shop.name, Sale.date_sale, Sale.count * Sale.price). \
        join(Book.publisher).join(Stock).join(Shop).join(Sale).filter(Publisher.name == name_publisher).all()
    if check_publisher:
        if query:
            for publisher in query:
                print(publisher.title, "|", publisher.name, "|", publisher.date_sale, "|", publisher[3])
        else:
            print("Данный издатель книги в магазинах не продавал")

    else:
        print("Данного издателя в базе нет")

