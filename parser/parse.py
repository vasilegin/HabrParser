from traceback import print_tb
import requests
import logging
import json

from utils.files import get_assets

config = get_assets('config')

def worker(i):
    url = config['url']['parse'].format(i)
    headers = {
    'User-Agent': config['headers']['User-Agent']
    }

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

    article = json.loads(r.text)
    
    with open(r'rez.text', 'w+', encoding='utf8') as f:
        json.dump(article ,f, indent=4,  ensure_ascii=False)
    print(r.text)
