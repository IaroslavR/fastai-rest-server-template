config = {
    "development": "api.config.DevelopmentConfig",
    "testing": "api.config.TestingConfig",
    "production": "api.config.ProductionConfig",
    "staging": "api.config.StagingConfig",
}


class Config(object):
    ENV = "default"
    TESTING = False


class ProductionConfig(Config):
    ENV = "production"


class StagingConfig(Config):
    ENV = "staging"


class DevelopmentConfig(Config):
    ENV = "development"
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
