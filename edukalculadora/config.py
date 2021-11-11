ENV ='prod'
if ENV == 'dev':
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI ='mysql+pymysql://newuser:password@localhost/calculadora'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///storage.db'
else:
    DEBUG = True
    DATABASE_URL='postgres://nhbzneqiflzggb:b99755d34395cca1275449d2b7fe1f311fcbc191e453ebe2ae7c4c75d04f5a11@ec2-44-199-40-188.compute-1.amazonaws.com:5432/de2megdttiguim'
    SQLALCHEMY_DATABASE_URI = DATABASE_URL.replace("://", "ql://", 1)

SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'calculadora'