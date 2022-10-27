from db.base import Session
from db.models import Article
import requests
import logging
import json
import os

from utils.files import get_assets

config = get_assets('config')
session = Session()
count = session.query(Article).count()

def worker(i):
    url = config['url']['parse'].format(i)
    headers = {
    'User-Agent': config['headers']['User-Agent']
    }
    global count

    try:
        r = requests.get(url, headers=headers)
        if r.status_code == 503:
            logging.critical("503 Error")
            raise SystemExit
        if r.status_code != 200:
            logging.info("Not found or in drafts")
            return 404
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

    _article = json.loads(r.text)
    article = Article(
        id = _article['id'],
        tP = _article['timePublished'],
        lang = _article['lang'],
        titleHtml = _article['titleHtml'],
        textHtml = _article['textHtml'],
        pL = _article['postLabels'],
        af = _article['author']['fullname'],
        ar = _article['author']['rating'],
        rC = _article['statistics']['readingCount'],
        tags = ','.join(tuple(tag['titleHtml'] for tag in _article['tags'])),
        classes = ','.join(tuple(tag['titleHtml'] for tag in _article['hubs']))
    )
    try:
        session.add(article)
        session.commit()
        count += 1
    except:
        session.rollback()
        # print("err")
        # raise

    os.system('cls||clear')
    print(count)