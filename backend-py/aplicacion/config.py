class Config(object):
    SECRET_KEY = 'f0faa2bed03b28e48544762d760aa169'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
    PATH_STORAGE = "/app/tmp_storage"
    ROOT_PATH = "/app"
    TIME_SESSION = 60000
  

class TestingConfig(Config):
    """
    Testing configurations 
    """
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://adminmysqlcnt@mysqlcnt:oF9OpN7B@mysqlcnt.mysql.database.azure.com:3306/pruebadesarrollo"
    ##SQLALCHEMY_DATABASE_URI = "mysql+pymysql://demo:Demo2020!@157.245.185.170:3306/bd_limpia_demo"
    SQLALCHEMY_POOL_RECYCLE = 200
    DEBUG = True
    TESTING = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REDIS_URL = "redis://157.245.185.170:6379/0"
    PATH_STORAGE = "/app/testing/upload"
    ROOT_PATH = "/app"
    TIME_SESSION = 60000
    SQLALCHEMY_POOL_RECYCLE=160
    API_BACKEND_CAPTCHA = "https://www.google.com/recaptcha/api/siteverify"  
    



class ProductionConfig(Config):
    """
    Production configurations
    """
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://demo:Demo2020!@157.245.185.170:3306/bd_limpia_demo"
    DEBUG = True
    TESTING = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REDIS_URL = "redis://157.245.185.170:6379/0"
    PATH_STORAGE = "/app/upload"
    ROOT_PATH = "/app"
    TIME_SESSION = 60000
    SQLALCHEMY_POOL_RECYCLE=160
    API_BACKEND_CAPTCHA = "https://www.google.com/recaptcha/api/siteverify"
    


app_config = {
    'testing': TestingConfig,
    'production': ProductionConfig
}