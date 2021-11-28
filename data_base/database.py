from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import models

class DataBase:
    def __init__(self, db_url):
        engine = create_engine(db_url)
        models.Base.metadata.create_all(bind=engine)
        self.maker = sessionmaker(bind=engine)