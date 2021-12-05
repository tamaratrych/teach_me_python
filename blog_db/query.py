from blog_db import models

# def author_tags(session, author_id):
#     author_articles = session.query(models.Article.id).filter(models.Author.id == author_id).all()
#     tags = []
#     for article in author_articles:
#         tag = session.query(models._article_tag.article_id).filter(models._article_tag.tag_id).all()
#         tags.extend(tag)
#     tags = set(tags)
#     tag_name = []
#     for itm in tags:
#         tag = session.query(models.Tag.name).filter(models.Tag.id == itm).all()
#         tag_name.extend(tag)
#     tag_name = set(tag_name)
#     return tag_name


# def get_authors_used_tag(session, tag_name):
#     tag_id = session.query(models.Tag.id).filter(models.Tag.name == tag_name).first()
#     articles_id = session.query(models._article_tag.article_id.distinct()).filter(models._article_tag.tag_id == tag_id).all()
#     authors_used_tag = [article.author.name for article in articles_id]
#     return authors_used_tag

def author_tags(session, author_id):
    tags_id = session.query(models.Article.tag_id).filter(models.Article.author_id == author_id).all()
    tags_id = set(tags_id)
    temp_tags = []
    for i in tags_id:
        tag = session.query(models.Tag.name).filter(models.Tag.id == tuple(i)[0]).all()
        tag = tuple(tag)
        temp_tags.extend(tag)
    temp_tags = set(temp_tags)
    tags = []
    for i in temp_tags:
        tags.append(tuple(i)[0])
    return tags


def get_authors_used_tag(session, tag_name):
    tag_id = session.query(models.Tag.id).filter(models.Tag.name == tag_name).first()
    articles_id = session.query(models.Article.id).filter(models.Article.tag_id == tag_id[0]).all()
    authors = []
    for i in articles_id:
        auth_id = session.query(models.Article.author_id).filter(models.Article.id == i[0]).first()
        authors.append(auth_id[0])
    authors = set(authors)
    author_names = []
    for i in authors:
        name = session.query(models.Author.name).filter(models.Author.id == i+1).first()
        surname = session.query(models.Author.surname).filter(models.Author.id == i+1).first()
        author_names.append(f"{tuple(name)[0]} {tuple(surname)[0]}")
    return author_names


