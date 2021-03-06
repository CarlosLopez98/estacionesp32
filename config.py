class Config:
    SECRET_KEY = "Estaseunallavesecreta"


class DevelopmentConfig(Config):
    DEBUG = True
    ENV = 'development'


class ProductionConfig(Config):
    DEBUG = False
    ENV = 'production'
    SERVER_NAME = 'carloslopez98.pythonanywhere.com'


config = {
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'default': DevelopmentConfig,
}
