import os


class Config:
    DEBUG = False
    SECRET_KEY = os.getenv('SECRET_KEY')

    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = int(os.getenv('MAIL_PORT'))
    MAIL_USE_TLS = bool(os.getenv('MAIL_USE_TLS'))
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_RECEIVERS = os.getenv('MAIL_DEFAULT_RECEIVERS').split(',')
    MAIL_DEFAULT_SENDER = tuple(os.getenv('MAIL_DEFAULT_SENDER').split(',', 1))

    # URL to redirect after sending the e-mail.
    REDIRECT_TO = os.getenv('REDIRECT_TO')


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True
