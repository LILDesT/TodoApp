from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#sqlite3
SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosapp.db'

"""
#postgresql
need pip install psycopg2-binary
SQLALCHEMY_DATABASE_URL = 'postgresql://postgresql:test1234!@localhost/TodoappDatabase'

№mysql
need pip install pymysql
SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:test1234!@127.0.0.1:3306/TodoappDatabase'
"""
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

