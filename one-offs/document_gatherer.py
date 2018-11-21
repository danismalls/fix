import json
from elasticsearch import Elasticsearch, helpers


class DocumentGather:

def __init__(self, urlstring='http://tellfinder-elasticsearch.uncharted.software:9200/', index = 'mx_ht_documents_2_sift_6.1'):
    self.urlstring = urlstring
    self.es = Elasticsearch(urlstring, verify_certs=False, timeout=560)
    self.index = index
