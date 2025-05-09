from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL

# SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://fastapi_test:fastapi_test_password@fastapi_test_db/db"
SQLALCHEMY_DATABASE_URL = URL.create(drivername="postgresql", username="fastapi_test",
                                     host="db", database="fastapi_test_db", password="fastapi_test_password")

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()
