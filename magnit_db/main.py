from parse import parse_page, parse_data
from class_magnit import Magnit
from magnit_db.data_base import data_base, fill_db


source = Magnit()
response = source.get_page(source.url)
products = set()
db_url = "sqlite:///magnit_db.db"
db = data_base.DataBase(db_url)
#print(1)

def main():
    parse_page(source, response, products)
    # print(2)
    # print(products)
    promo_dict = parse_data(source, products)
    # print(3)
    # print(promo_dict)
    session = db.maker()
    fill_db.fill_data(session, promo_dict)
    session.close()
    # print(4)


if __name__ == "__main__":
    main()