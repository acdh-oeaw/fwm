import requests
from django.conf import settings
from dateutil.parser import isoparse
from requests.exceptions import ConnectionError, MissingSchema

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


def get_zotero_item(zotero_key, base_url=ZOTERO_URL):
    url = f"{base_url}/{zotero_key}"
    r = requests.get(url)
    data = r.json()
    try:
        zotero_date = isoparse(data['meta'].get('parsedDate'))
    except TypeError:
        zotero_date = None
    return {
        "zotero_key": zotero_key,
        "zotero_title": data['data'].get('title', "no title provided"),
        "zotero_data": data['data'],
        "zotero_date": zotero_date,
        "zotero_creator": data['meta'].get('creatorSummary', "NN"),
    }
