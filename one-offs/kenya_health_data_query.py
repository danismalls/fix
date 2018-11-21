import json
from elasticsearch import Elasticsearch, helpers

class KenyaTweetGatherer:
    
    def __init__(self, urlstring='https://' + 'ic-kenya-darpa-ro' + ':' + 'Hbq7f3wApsetf4sw' + '@' + \
'c3b40d472cc1e8bc18ea4143fd81e66b.us-east-1.aws.found.io:9243', index = 'ic-ke-health-darpa'):
        self.urlstring = urlstring
        self.es = Elasticsearch(urlstring, verify_certs=False, timeout=360)
        self.index = index
        
    def get_n_items(self, begin, end, lang=None):
        
        if lang:
            query = self._format_query(begin, end, lang=lang)
            
        else:
            query = self._format_query(begin, end)

        number_of_docs = self.es.count(index=self.index, body=query)['count']
        return number_of_docs

    
    def _format_query(self, begin, end, lang=None):
        
        if lang:
            query_string = 'doc.place.country_code: KE AND doc.lang: ' + lang
            
        else:
            query_string = 'doc.place.country_code: KE'
        
        query = {
          "query": {
            "bool": {
              "must": [
                {
                  "query_string": {
                    "query": query_string,
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
    
    def get_data(self, begin, end, lang=None):
        
        query = self._format_query(begin, end, lang)
        
        results = helpers.scan(self.es, index=self.index, query=query)
        
        number_of_docs = self.get_n_items(begin=begin,end=end,lang=lang)

        data = []
        count = len(data)
        for r in results:
            data.append(r)
            if len(data) % 10000 == 0:
                print('fraction complete:', float(len(data))/number_of_docs)
                
        return data
