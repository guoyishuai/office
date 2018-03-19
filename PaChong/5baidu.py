# -*- coding:utf-8 -*-
import requests
keyword = "郭义帅"
url= "http://www.baidu.com/s"
try:
    kv = {'wd':'keyword'}
    r= requests.get(url, params=kv)
    print (r.request.url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print len(r.text)

    print r.text[1000:20000]

except:
    print ("爬取失败")
