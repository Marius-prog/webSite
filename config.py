import os

SQLALCHEMY_TRACK_MODIFICATIONS = True


class BaseConfig(object):
    DEBUG = False


# class DevConfig(BaseConfig):
#     DEBUG = True
#     SQLALCHEMY_DATABASE_URI = 'sqlite:///data/db.sqlite'


class ProdConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgres://xobzipcncvwotj:985b1f28540a1934d60bf8bc7bace58da2430f1f82c21be3613f531cdc67466f@ec2-54-217-204-34.eu-west-1.compute.amazonaws.com:5432/dafi5uhd5oebg4'

class HerokuConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
