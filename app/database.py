from sqlalchemy import create_engine, MetaData 

SQLALCHEMY_DATABASE_URL = "sqllite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connnect_args={"check_same_thread": False})
metadata = MetaData()