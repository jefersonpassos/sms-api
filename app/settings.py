class Config(object):
    DEBUG = True
    TESTING = True
    DATABASE_URI = 'user/pass@perfp'
    APPLICATION_ROOT = '/api/sms'
    MS_HOST = "10.58.0.222"
    MS_DB = "database"
    MS_USER = "user"
    MS_PASS = "pass"

class Production(Config):
    DEBUG = False
    DATABASE_URI = 'performance/performance@perfp'

class Development(Config):
    DEBUG = True
    
class Testing(Config):
    TESTING = True
