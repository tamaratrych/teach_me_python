from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from magnit_db.data_base import model

class DataBase:
    def __init__(self, db_url):
        engine = create_engine(db_url)
        model.Base.metadata.create_all(bind=engine)
        self.maker = sessionmaker(bind=engine)
