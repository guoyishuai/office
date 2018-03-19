# -*- coding:utf-8 -*-

import requests
url = "http://m.ip138.com/ip.asp?ip="
try:

    r = requests.get(url + "202.204.80.113")

    #r.raise_for_status()

    r.encoding = r.apparent_encoding

    print r.text
except:
    print "爬取失败"