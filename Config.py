import os

class dbConfig:
    DEBUG = True  # Set this to True for development, or False for production
    MYSQL_DATABASE_USER = os.environ.get('MYSQL_DATABASE_USER')
    MYSQL_DATABASE_PASSWORD = os.environ.get('MYSQL_DATABASE_PASSWORD')
    MYSQL_DATABASE_DB = os.environ.get('MYSQL_DATABASE_DB')
    MYSQL_DATABASE_HOST = os.environ.get('MYSQL_DATABASE_HOST')
    MYSQL_DATABASE_PORT = 3306
    MYSQL_DATABASE_SCHEMA = os.environ.get('MYSQL_DATABASE_SCHEMA')
