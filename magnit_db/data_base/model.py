from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import (
    Column,
    String,
    Integer,
)

Base = declarative_base()

class MagnitPromo(Base):
    __tablename__ = "magnit_promo"
    id = Column(Integer, primary_key=True, autoincrement=True)
    promo_url = Column(String, unique=True, nullable=False)
    promo_title = Column(String, unique=True, nullable=True)
