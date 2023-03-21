"""Параметры подключения к БД """
driver = "postgresql"
login_db = "postgres"
password_db = "123"
host_db = "localhost"
port_db = "5432"
name_db = "netology_db"

DSN_connect = f'{driver}://{login_db}:{password_db}@{host_db}:{port_db}/{name_db}'
