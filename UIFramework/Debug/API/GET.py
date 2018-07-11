# import requests
#
# #res = requests.get('https://github.com/timeline.json')
# res = requests.get("http://115.29.234.80:8201/WebReport/sytlj.jsp")
# print(res.text)

# import requests
# def get(url,params=None,**kwargs):
#     kwargs.setdefault('allow_redirects',True)
#     return requests('get',url,params=params,**kwargs)
#
# res = requests.get(url='http://yuedu.baidu.com/ebook/3c0077aaa32d7375a41780bb',
#                    params={
#                        #'username':'nieliangcai',
#                        '_searchquery':'selenium-python%D7%D4%B6%AF%BB%AF%B2%E2%CA%D4'
#                    })
# print(res.url)

import requests

res = requests.get('http://www.bing.com')
#print(res.text)
print(res.status_code)
print(res.url)
print(res.headers)