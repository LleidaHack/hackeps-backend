class Config(object):
    DEBUG = False
    TESTING = False
    KEY = 'kiwi/conf/key.json'
    SDK = 'kiwi/conf/sdk.json'
    COLLECTION_ROOT = u'hackeps-2021'
    USERS = u'users'
    TEAMS = u'teams'

class ProductionConfig(Config):
    DB_MODE = u'prod'

class DevelopmentConfig(Config):
     ENV="development"
     DB_MODE = u'dev'

class TestingConfig(Config):
    ENV="testing"
    DB_MODE = u'test'
    TESTING = True
