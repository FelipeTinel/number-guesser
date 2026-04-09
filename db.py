from sqlalchemy import create_engine
from sqlalchemy.orm import sessiomaker, declarative_base

DATABASE_URL =  'postgresql://tinel:2222@localhost:5432/number_db'