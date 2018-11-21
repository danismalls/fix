import json
from elasticsearch import Elasticsearch, helpers

class DocumentGather:

    def __init__(self, urlstring='http://tellfinder-elasticsearch.uncharted.software:9200/', index = 'mx_ht_documents_2_sift_6.1'):
        self.urlstring = urlstring
        self.es = Elasticsearch(urlstring, verify_certs=False, timeout=560)
        self.index = index

    def get_n_items(self, begin, end):

        #if lang:
            #query = self._format_query(begin, end, query_str, lang=lang)

        query = self._format_query()

        number_of_docs = self.es.count(index=self.index, body=query)['count']
        return number_of_docs


    def _format_query(self):

        query = {
                  "size": 0,
                  "aggs" : {
                    "sources": {
                      "terms": {
                        "field":"feature.site_name",
                        "size": 0
                      }
                    }
                  }
                }


        return query

    def get_data(self, begin, end, query_str, lang=None):

        query = self._format_query(begin, end, query_str, lang)

        results = helpers.scan(self.es, index=self.index, query=query)

        number_of_docs = self.get_n_items(begin=begin,end=end,query_str=query_str, lang=lang)

        data = []
        count = len(data)
        for r in results:
            data.append(r)
            if len(data) % 10000 == 0:
                print('fraction complete:', float(len(data))/number_of_docs)

        return data
