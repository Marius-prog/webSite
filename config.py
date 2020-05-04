class BaseConfig(object):
    DEBUG = False


class DevConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data/db.sqlite'


class ProdConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgres://pmmxsrzkowyest:6d4cd165091a74ff23363c9843fc757ad81095bf247bd7134e89657b1ac8c4fb@ec2-46-137-156-205.eu-west-1.compute.amazonaws.com:5432/d655jq2rf6onbs'
