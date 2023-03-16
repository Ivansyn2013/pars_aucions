import sys

from dotenv import dotenv_values
import logging


class Config(object):
    TESTING = False


class DevelopmentConfig(Config):
    logging.basicConfig(level=logging.DEBUG)
    config = dotenv_values('.env')
    TESTING = True
    DB_PASS = config['DB_PASS']
    DB_USER = config['DB_USER']
    DB_PORT = config['DB_PORT']
    # DATABASE_URI = ''
    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASS}@localhost:{DB_PORT}/amt'
    SQLALCHEMY_MODIFICATIONS = False
    SECRET_KEY = 'abcdefg123456'

# class DeployConfig(Config):
#     logging.basicConfig(level=logging.WARNING)
#     config = dotenv_values(".env")
#     TESTING = config['TESTING']
#     SQLALCHEMY_DATABASE_URI = config['SQLALCHEMY_DATABASE_URI']
#     SQLALCHEMY_MODIFICATIONS = config['SQLALCHEMY_MODIFICATIONS']
#     SECRET_KEY = config['SECRET_KEY']
