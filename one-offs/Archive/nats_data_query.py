import json
from elasticsearch import Elasticsearch, helpers

class TweetGatherer:

    def __init__(self, urlstring='http://tellfinder-elasticsearch.uncharted.software:9200/', index = 'mx_ht_documents_2_sift_6.1'):
        self.urlstring = urlstring
        self.es = Elasticsearch(urlstring, verify_certs=False, timeout=560)
        self.index = index

    def get_n_items(self, begin, end, query_str, lang=None):

        if lang:
            query = self._format_query(begin, end, query_str, lang=lang)

        else:
            query = self._format_query(begin, end, query_str)

        number_of_docs = self.es.count(index=self.index, body=query)['count']
        return number_of_docs


    def _format_query(self, begin, end, query_str, lang=None):

        query = {
          "query": {
            "bool": {
              "must": [
                {
                  "query_string": {
                    "query": query_str,
                    "analyze_wildcard": True
                  }
                },
                {
                  "range": {
                    "norm.timestamp": {
                      "gte": begin+"T00:00:00.000",
                      "lte": end+"T00:00:00.000",
                      "format": "yyyy-MM-dd\'T\'HH:mm:ss.SSS"
                    }
                  }
                }
              ],
              "must_not": []
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
