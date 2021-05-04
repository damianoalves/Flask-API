# -*- coding: utf-8 -*-
import os


class Config:

    # project root directory
    BASE_DIR = os.path.join(os.pardir, os.path.dirname(__file__))
    SECRET_KEY = os.environ.get("SECRET_KEY")

    # Flask Configuration
    # --------------------------------------------------------------------
    DEBUG = False
    TESTING = False
    PORT = 8000

    # log file path
    # --------------------------------------------------------------------
    enable_access_log = False
    log_socket_host = "127.0.0.1"
    log_socket_port = 514

    # redis main
    # --------------------------------------------------------------------
    REDIS_HOST = "redis"  # docker network
    REDIS_PORT = 6379
    REDIS_DB = 0
    REDIS_PASSWD = ''

    # sqlalchemy database main
    # --------------------------------------------------------------------
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ENGINE_OPTIONS = {
        'executemany_mode': 'batch',
        'client_encoding': 'utf8',
        'case_sensitive': False,
        'echo': True,
        'echo_pool': True
    }

    # SMTP server main
    # --------------------------------------------------------------------
    SERVER_EMAIL = 'Damiano <damiano.alves@gmail.com>'
    DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', SERVER_EMAIL)
    EMAIL_HOST = os.environ.get('EMAIL_HOST')
    EMAIL_PORT = os.environ.get('EMAIL_PORT')
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')


class DevelopmentConfig(Config):

    ENV = os.environ.get("FLASK_ENV", "development")
    DEBUG = True
    ASSETS_DEBUG = True


class TestingConfig(Config):

    ENV = os.environ.get("FLASK_ENV", "testing")
    DEBUG = True
    TESTING = True


class ProductionConfig(Config):

    ENV = os.environ.get("FLASK_ENV", "production")
    DEBUG = False
    USE_RELOADER = False


settings = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig,
}