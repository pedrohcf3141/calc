ENV ='prod'
if ENV == 'dev':
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI ='mysql+pymysql://newuser:password@localhost/calculadora'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///storage.db'
else:
    DEBUG = True
    DATABASE_URL='postgres://cqegbyasbharhl:a06dcedba054a9b0dfd9f47ff0dc5d474a32a6bf66c2519e229a3f6b5ecd3961@ec2-3-218-92-146.compute-1.amazonaws.com:5432/ddhlh26vr9o0pu'
    SQLALCHEMY_DATABASE_URI = DATABASE_URL.replace("://", "ql://", 1)

SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'calculadora'