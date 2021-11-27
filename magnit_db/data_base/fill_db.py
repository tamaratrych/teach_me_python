from magnit_db.data_base import model

def fill_data(session, promo_dict):
    count = 0
    for url, title in promo_dict.items():
        line = model.MagnitPromo(promo_url=url, promo_title=title)
        session.add(line)
        count += 1
        if count == 10:
            session.commit()
            count = 0
        session.commit()