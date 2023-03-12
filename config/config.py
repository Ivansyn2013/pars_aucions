import sys

from dotenv import dotenv_values
import logging


class Config(object):
    TESTING = False


class DevelopmentConfig(Config):
    logging.basicConfig(level=logging.DEBUG)
    TESTING = True
    # DATABASE_URI = ''
    SQLALCHEMY_DATABASE_URI = 'postgresql://user:123@localhost:5432/amt'
    SQLALCHEMY_MODIFICATIONS = False
    SECRET_KEY = 'abcdefg123456'

# class DeployConfig(Config):
#     logging.basicConfig(level=logging.WARNING)
#     config = dotenv_values(".env")
#     TESTING = config['TESTING']
#     SQLALCHEMY_DATABASE_URI = config['SQLALCHEMY_DATABASE_URI']
#     SQLALCHEMY_MODIFICATIONS = config['SQLALCHEMY_MODIFICATIONS']
#     SECRET_KEY = config['SECRET_KEY']
