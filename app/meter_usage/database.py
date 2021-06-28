
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base  # type: ignore
from sqlalchemy.orm import sessionmaker  # type: ignore
from app.meter_usage.config import RDS_HOST, RDS_PORT, RDS_PASSWORD, RDS_USER, RDS_DB, RDS_DBTYPE

SQLALCHEMY_DATABASE_URI = f"{RDS_DBTYPE}://{RDS_USER}:{RDS_PASSWORD }@{RDS_HOST}:{RDS_PORT}/{RDS_DB}"

engine = create_engine(SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

session = None


def get_session():
    ##maintaining the database session globally
    global session
    if not session:
        session = SessionLocal()
        try:
            return session
        finally:
            session.close()
    else:
        return session
