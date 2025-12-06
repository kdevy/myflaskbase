import os

class BaseConfig:
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "mysql+pymysql://{user}:{password}@{host}/{dbName}?charset=utf8".format(
            user = os.getenv('DB_USER'),
            password = os.getenv('DB_PASS'),
            host = os.getenv('DB_HOST'),
            dbName = os.getenv('DB_NAME')
        ))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LANGUAGES = ['ja', 'ja_JP', 'en']
    BABEL_DEFAULT_LOCALE = 'ja'
    BABEL_TRANSLATION_DIRECTORIES = "translations"


class DevConfig(BaseConfig):
    DEBUG = True


class ProdConfig(BaseConfig):
    DEBUG = False