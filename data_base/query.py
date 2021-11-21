from data_base import models

def author_tags(session, author_id):
    author_articles = session.query(models.Article.id).filter(models.Author.id == author_id).all()
    tags = []
    for article in author_articles:
        tag = session.query(models._article_tag.article_id).filter(models._article_tag.tag_id).all()
        tags.extend(tag)
    tags = set(tags)
    tag_name = []
    for itm in tags:
        tag = session.query(models.Tag.name).filter(models.Tag.id == itm).all()
        tag_name.extend(tag)
    tag_name = set(tag_name)
    return tag_name

def get_authors_used_tag(session, tag_name):
    tag_id = session.query(models.Tag.id).filter(models.Tag.name == tag_name).first()
    articles_id = session.query(models._article_tag.article_id.distinct()).filter(models._article_tag.tag_id == tag_id).all()
    authors_used_tag = [article.author.name for article in articles_id]
    return authors_used_tag

   #author_id = session.query(models.Tag.articles.author.id.distinct()).filter(models.Tag.name == tag_name).all()
    #session.query(models.Author.name).filter(models.Author.id in author_id)

