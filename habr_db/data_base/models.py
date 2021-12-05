from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Table,
    DateTime,
)

Base = declarative_base()


_article_tag = Table(
    "article_tag",
    Base.metadata,
    Column("article_id", Integer, ForeignKey("article.id")),
    Column("tag_id", Integer, ForeignKey("tag.id")),
)


class Author(Base):
    __tablename__ = 'author'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=False)
    link = Column(String(50), unique=True)


class Tag(Base):
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True)


class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(250), unique=False)
    published_date = Column(DateTime)
    tags = relationship("Tag", secondary='article_tag', backref='article')