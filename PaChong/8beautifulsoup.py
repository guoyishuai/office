# -*- coding:utf-8 -*-

import requests
from bs4 import  BeautifulSoup
r = requests.get("http://tieba.baidu.com/f?kw=%BD%A3%C0%B4&fr=ala0&loc=rec")
demo = r.text
soup = BeautifulSoup(demo, "html.parser")

soup.prettify()

#print soup.prettify()
for link in soup.find_all('a'):
    print link.get('title')
