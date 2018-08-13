import os
from datetime import timedelta

SECRET_KEY=os.urandom(24)
#PERMANENT_SESSION_LIFETIME=True

SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:123456@localhost:3306/ktwd?charset=utf8'
SQLALCHEMY_TRACK_MODIFICATIONS=False