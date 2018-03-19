# -*- coding:utf-8 -*-
import requests
url = "https://www.amazon.cn/dp/B0058XHR28/ref=gs_rnk_wdgt_301?_encoding=UTF8&m=A2EDK7H33M5FFG&pf_rd_p=5acbd3a5-ab5e-4972-8f72-420e3a40f110&pf_rd_s=merchandised-search-8&pf_rd_t=101&pf_rd_i=1484186071&pf_rd_m=A1AJ19PSB66TGU&pf_rd_r=D58B0EYAHCBA76GMMBJ9&pf_rd_r=D58B0EYAHCBA76GMMBJ9&pf_rd_p=5acbd3a5-ab5e-4972-8f72-420e3a40f110"
try:
    kv = {'user-agent':'Mozilla/5.0'}
    r= requests.get(url, headers=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print r.text[1:1000]

except:
    print ("爬取失败")
