import json
import jmespath

class JMESPathExtractor(object):
    def extract(self,query=None,body=None):
        try:
            return jmespath.search(query,json.loads(body))
        except Exception as e:
            raise ValueError('Invalid query: '+query+":" +str(e))


if __name__=="__main__":
    from utils.client import HTTPClient
    res = HTTPClient(url='http://115.29.234.80:8201/WebReport/login.jsp?username=',method='GET').send()
    #print(res.text)
    #print(jmespath.search(expression='Server'))
    status_code = res.status_code
    print(status_code)

    j = JMESPathExtractor()