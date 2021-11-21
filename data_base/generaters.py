import random

from data_base import models
import data


def fill_authors(session):
    for itm in range(100):
        author_itm = models.Author(name=random.choice(data.names), surname=random.choice(data.surnames), blog_id=itm+1)
        session.add(author_itm)
    session.commit()


def fill_blogs(session):
    for itm in range(100):
        blog_itm = models.Blog(title=f"Блог #{itm+1} - {random.choice(data.title_blog)}")
        session.add(blog_itm)
    session.commit()


def fill_tags(session):
    for itm in range(30):
        tag_itm = models.Tag(name=data.tags[itm])
        session.add(tag_itm)
    session.commit()


def fill_articles(session):
    for author in range(100):
        num_articles = random.randint(50, 100)
        for itm in range(num_articles):
            article_itm = models.Article(title=f'{data.title_article[itm]} {data.title_article[random.randint(0, 100)]}',
            author_id=author, blog_id=author)
            session.add(article_itm)
    session.commit()


def fill_article_tag(session):
    num_articles = models.Article.count_articles(session)
    for article in range(num_articles):
        num_tags = random.randint(3, 10)
        tags = set()
        for itm in range(num_tags):
            if itm not in tags:
                article_tag_itm = models._article_tag(article_id=article, tag_id=itm)
                tags.add(itm)
            else:
                continue
            session.add(article_tag_itm)
    session.commit()


def fill_db(session):
    fill_blogs(session)
    fill_authors(session)
    fill_tags(session)
    fill_articles(session)
    fill_article_tag(session)

