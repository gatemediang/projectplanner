from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#username = "root"
#password = ""
#database = "ticketing"
#host = "127.0.0.1"

#SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{username}:{password}@{host}/{database}"
#engine = create_engine(SQLALCHEMY_DATABASE_URL)


# postgresql
username = "postgres"
password = "olog1000"
host = "localhost"
database = "ticketapp"
SQLALCHEMY_DATABASE_URL = f"postgresql://{username}:{password}@{host}:5432/{database}"

#engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'sslmode':'require'})

engine = create_engine(SQLALCHEMY_DATABASE_URL)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()