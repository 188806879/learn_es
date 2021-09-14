#!coding:utf-8
import datetime
import time
import traceback
import json
from ssl import create_default_context
from elasticsearch import Elasticsearch

body = {
    "query": {
        "match_all": {}
    }
}

client = Elasticsearch(
    ['10.67.19.56:9200'],
    # turn on SSL
    use_ssl=True,
    http_auth=("elastic",'123456'),
    # make sure we verify SSL certificates
    verify_certs=False
)
print client.search(index="test", body=body)
