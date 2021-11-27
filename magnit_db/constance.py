import re


url = "https://magnit.ru/promo/"
pattern_url = re.compile(r"href=\"(/promo\S+)\"")
pattern_tittle = re.compile(r"<div class=\"action__title\">(.+)</div>")
