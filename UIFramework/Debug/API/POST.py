# import requests
#
# res = requests.post('http://httpbin.org/post')
# print(res.text)

# import requests
# # def POST(url,data=None,json=None,**kwargs):
# #     return requests('post',url,data=data,param=json,**kwargs)
#
# res = requests.post(url='http://m.cyw.com/index.php?m=api&c=cookie&a=setcity',
#                     data={'cityId':438})
# print(res.json())

# import requests
# import json
#
# data = {'username':'13484545195','password':'123456'}
#
# res = requests.post(
#     url='http://m.cyw.com/index.php?m=api&c=login&a=authorized',
#     data=data)
# print(json.dumps(res.text))
# print(res.json())

import requests
url = 'http://www.shwzoo.com/tools/submit_ajax.ashx?action=user_login'
data = {'username':'2397244682@qq.com','password':'123456'}
res = requests.post(url=url,data=data)
print(res.status_code)
print(res.headers)
print(res.url)
#print(res.text)
print(res.json())
