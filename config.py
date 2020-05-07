import os

SQLALCHEMY_TRACK_MODIFICATIONS = True


class BaseConfig(object):
    DEBUG = False


class DevConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data/db.sqlite'


class ProdConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgres://bonbtmgvqetlra:181b2937b2b3b5dc8f1a6dc8d9dbbd2c35ea9ee1abdc347a2b572d28cf7f3f6e@ec2-54-217-204-34.eu-west-1.compute.amazonaws.com:5432/den7pape66kgnp'


class HerokuConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
