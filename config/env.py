import os
from os import environ

CSRF_ENABLED = environ.get('CSRF_ENABLED', 'True')
CSRF_SESSION_KEY = environ.get('CSRF_SESSION_KEY', os.urandom(32))
SQLALCHEMY_TRACK_MODIFICATIONS = environ.get('SQLALCHEMY_TRACK_MODIFICATIONS', 'False')

DB_DRIVER = environ.get('DB_DRIVER', 'mysql+pymysql')
DB_USER = environ.get('DB_USER', 'root')
DB_PASSWORD = environ.get('DB_PASSWORD', '')
DB_HOST = environ.get('DB_HOST', 'localhost')
DB_PORT = environ.get('DB_PORT', 3306)
DB_NAME = environ.get('DB_NAME', 'flask')
DB_CHARSET = environ.get('DB_CHARSET', 'utf8mb4')
