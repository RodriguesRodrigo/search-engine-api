class Config:
    APP_PORT = 5000
    DEBUG = False
    SECRET_KEY = b"X\xca\x1e\xb2\xd3 m3\xa8AI\x1e\xcd{\xfe\xb8"


class DevelopmentConfig(Config):
    DEBUG = True
    FLASK_ENV = "development"


class TestConfig(Config):
    TESTING = True
    FLASK_ENV = "testing"


class ProductionConfig(Config):
    DEBUG = False
    FLASK_ENV = "production"


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestConfig,
    "default": DevelopmentConfig
}
