# Проектируем базу данных мультиблога
# todo: Должен быть объект публикации
# todo: Должны быть теги
# todo: Объект Автора
# todo: Объект блога


# todo:  Заполнить базу минимум 100 авторами, у каждого автора от 50 до 100 статей, в которых от 3х тегов
# todo: Составить запрос и определить все теги использованые этим автором
# todo: Составить запрос и получить всех авторов которые использовали "Этот тег"

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Table,
)

Base = declarative_base()


_article_tag = Table(
    "article_tag",
    Base.metadata,
    Column("article_id", Integer, ForeignKey("article.id")),
    Column("tag_id", Integer, ForeignKey("tag.id")),
    #UniqueConstraint('article_id', 'tag_id')
)


class Author(Base):
    __tablename__ = 'author'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), unique=False)
    surname = Column(String(30), unique=False)
    blog_id = Column(Integer, ForeignKey("blog.id"), nullable=False)


class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), unique=False)
    blog_id = Column(Integer, ForeignKey("blog.id"), nullable=False)
    author_id = Column(Integer, ForeignKey("author.id"), nullable=False)
    author = relationship(Author, backref='articles')
    tags = relationship("Tag", secondary=_article_tag, backref='articles')

    def count_articles(self, session):
        return session.query(Article.id).count()


class Blog(Base):
    __tablename__ = "blog"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(25), unique=True)


class Tag(Base):
    __tablename__ = "tag"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), unique=True)
