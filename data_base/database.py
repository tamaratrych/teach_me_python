from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from data_base import models

class DataBase:
    def __init__(self, db_url):
        engine = create_engine(db_url)
        models.Base.metadata.create_all(bind=engine)
        self.maker = sessionmaker(bind=engine)

db_url = "sqlite:///magnit_db.db"
db = DataBase(db_url)
session = db.maker()