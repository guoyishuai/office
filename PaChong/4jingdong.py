# -*- coding:utf-8 -*-
import requests , re
url = "https://www.bilibili.com/video/av19956343"
try:
    kv = {'user-agent':'Mozilla/5.0'}
    r= requests.get(url, headers=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    #print r.text
    UrlCompare = re.compile('video/av\d+')
    # urls = UrlCompare.search(r.text)
    # print (urls.group(0))
    urls = UrlCompare.findall(r.text)
    print (urls)
except Exception, e:
    print ("爬取失败")
    print (str(e))
