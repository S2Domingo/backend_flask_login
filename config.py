import os

DB_USER_NAME    = os.getenv('DB_USER')
DB_USER_PASSWD  = os.getenv('DB_PASSWD')
DB_HOST         = os.getenv('DB_HOST')
DB_NAME         = os.getenv('DB_NAME')

SQLALCHEMY_DATABASE_URI = 'mysql://{}:{}@{}/{}?charset=utf8'.format(DB_USER_NAME, DB_USER_PASSWD, DB_HOST, DB_NAME)
SQLALCHEMY_TRACK_MODIFICATIONS = False