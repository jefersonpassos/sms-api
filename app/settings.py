class Config(object):
    DEBUG = True
    TESTING = True
    DATABASE_URI = 'performance/performance@perfp'
    APPLICATION_ROOT = '/api/sms'
    MS_HOST = "10.58.0.222"
    MS_DB = "FRAMEWORK"
    MS_USER = "FRAMEWORK"
    MS_PASS = "conecta@2015"

class Production(Config):
    DEBUG = False
    DATABASE_URI = 'performance/performance@perfp'

class Development(Config):
    DEBUG = True
    
class Testing(Config):
    TESTING = True