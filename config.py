# edit the URI below to add your RDS password and your AWS URL
# The other elements are the same as used in the tutorial
# format: (user):(password)@(db_identifier).amazonaws.com:3306/(db_name)

SQLALCHEMY_TRACK_MODIFICATIONS = False
# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://admin:masters123@masters-10-15.ccegwawiyjmw.us-west-2.rds.amazonaws.com:3306/masters1015'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://admin:masters123@masters-live.ccegwawiyjmw.us-west-2.rds.amazonaws.com:3306/masterslive'

# Uncomment the line below if you want to work with a local DB
# SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

SQLALCHEMY_POOL_RECYCLE = 3600

WTF_CSRF_ENABLED = True
SECRET_KEY = 'AKIAIXAHQMLW2BGQXWJA'

USERNAME = 'masters'
PASSWORD = 'greenjacket'
