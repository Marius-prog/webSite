import os
SQLALCHEMY_TRACK_MODIFICATIONS = True

class BaseConfig(object):
    DEBUG = False



class ProdConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = ''



