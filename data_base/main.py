from generaters import fill_db
from database import DataBase
import query
import models


def main():
    db_url = "sqlite:///blog_db.db"
    db = DataBase(db_url)
    session = db.maker()
    fill_db(session)

    author_tags = query.author_tags(session, 5)
    print(author_tags)

    # authors_used_tag = query.get_authors_used_tag(session, "крепость")
    # print(authors_used_tag)


if __name__ == '__main__':
    main()