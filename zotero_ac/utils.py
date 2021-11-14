import requests
from requests.exceptions import ConnectionError, MissingSchema
from django.conf import settings

ZOTERO_URL = getattr(settings, 'ZOTERO_URL')


def search_zotero(query_string, url=ZOTERO_URL):
    query_params = {
        'q': query_string
    }
    try:
        r = requests.get(url, params=query_params)
    except (ConnectionError, MissingSchema) as e:
        print(e)
        return []
    if r.status_code != 200:
        return []
    else:
        result = [
            {
                "zotero_key": x['data'].get('key', 'NOKEY'),
                "zotero_title": x['data'].get('title', "no title provided"),
                "zotero_date": x['meta'].get('parsedDate'),
                "zotero_creator": x['meta'].get('creatorSummary', "NN"),
                "zotero_data": x
            } for x in r.json()
        ]
        return result


def get_zotero_item(zotero_key):
    url = f"{ZOTERO_URL}/{zotero_key}"
    r = requests.get(url)
    data = r.json()
    return {
        "zotero_key": zotero_key,
        "zotero_title": data['data'].get('title', "no title provided"),
        "zotero_data": data['data'],
        "zotero_date": data['meta'].get('parsedDate'),
        "zotero_creator": data['meta'].get('creatorSummary', "NN"),
    }
