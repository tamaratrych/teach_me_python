from generaters import fill_db
from database import DataBase
import query


def main():
    db_url = "sqlite:///blog_db.db"
    db = DataBase(db_url)
    session = db.maker()
    fill_db(session)

    author_tags = query.author_tags(session, 5)



if __name__ == '__main__':
    main()