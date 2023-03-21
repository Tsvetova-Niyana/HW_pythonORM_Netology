import sqlalchemy
from sqlalchemy.orm import sessionmaker
from function import load_db, create_tables, search_sale_by_publisher
from connect_db import DSN_connect

if __name__ == '__main__':
    DSN = DSN_connect
    engine = sqlalchemy.create_engine(DSN)
    create_tables(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    load_db(session)

    session.commit()

    print("Поиск продаж книг издателя в магазинах: ")

    search_sale_by_publisher(session)

    session.close()
