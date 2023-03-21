import sqlalchemy
from sqlalchemy.orm import sessionmaker
from function import load_db, create_tables, search_sale_by_publisher
from connect_db import DSN_connect

if __name__ == '__main__':
    # Подключение к БД
    DSN = DSN_connect
    engine = sqlalchemy.create_engine(DSN)

    # Создание таблиц
    create_tables(engine)

    # Создание сессии
    Session = sessionmaker(bind=engine)
    session = Session()

    # Загрузка данных в БД
    load_db(session)

    # Фиксация внесенных изменений
    session.commit()

    print("Поиск продаж книг издателя в магазинах: ")

    # Вызов функции поиска магазинов по характеристикам издателя
    search_sale_by_publisher(session)

    # Закрытие сессии
    session.close()
