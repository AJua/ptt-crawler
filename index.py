from elasticsearch7 import Elasticsearch
from datetime import datetime, timedelta
import json
import glob
import os

es = Elasticsearch(
    [ os.environ.get('ELASTIC_HOST') ],
    http_auth=(os.environ.get('ELASTIC_USER'), os.environ.get('ELASTIC_PASSWORD')),
    scheme=os.environ.get('ELASTIC_PROTOCOL'),
    port=os.environ.get('ELASTIC_PORT'),
)

ELASTIC_INDEX = "ptt"

def index_data(file):
    with open(file) as f:
        data = json.load(f)
        for a in data['articles']:
            try: 
                a['timestamp'] = datetime.strptime(a['date'], '%a %b  %d %H:%M:%S %Y') + timedelta(hours=-8)
                res = es.index(index=ELASTIC_INDEX, id=a['article_id'], body=a)
            except Exception as e: 
                print(a['article_id'])
                print(e)

doc = {
    'author': 'kimchy',
    'content': 'Elasticsearch: cool. bonsai cool.',
    'timestamp': datetime.now() + timedelta(hours=-8),
}

res = es.index(index=ELASTIC_INDEX, id=1, body=doc)

for file in glob.glob('./*.json'):
    try: 
        index_data(file)
    except Exception as e: 
        print(file)
        print(e)

res = es.get(index=ELASTIC_INDEX, id=1)
print(res['_source'])

es.indices.refresh(index=ELASTIC_INDEX)

res = es.search(index=ELASTIC_INDEX, body={"query": {"match_all": {}}})
print("Got %d Hits:" % res['hits']['total']['value'])
# for hit in res['hits']['hits']:
    # print("%(timestamp)s %(author)s: %(content)s" % hit["_source"])
