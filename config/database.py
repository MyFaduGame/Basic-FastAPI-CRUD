from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("postgresql://postgres:admin@localhost/fastapi_basic")
sessionlocal = sessionmaker(bind=engine,autocommit=False,autoflush=False)
Base=declarative_base()

def get_db():
    db = sessionlocal()

    try:
        yield db
    finally:
        db.close()