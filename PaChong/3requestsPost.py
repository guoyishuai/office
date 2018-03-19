# -*- coding: utf-8 -*-
import  requests

payload = {'key1':'value1','key2':'value2'}
r = requests.post('http://www.baidu.com/post',data = payload)
#r = requests.post('http://httpbin.org/post',data = payload)
print (r.text)
print r.url

url = ""

try:
    r = requests.get(url, timeout= 10)
    r.raise_for_status()
    r.enconding = r.apparent_encoding
    reutrn r.text

except:
    return "异常"
