# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[2].string])

def printUnivList(ulist, num):
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    print tplt.format("paiming","xueixao","shengfen", unichr(12288))
    for i in range(num):
        u = ulist[i]
        #print u[0], u[1], u[2]
        u.decoding = "utf-8"
        print tplt.format(u[0], u[1], u[2], unichr(12288))
    print ("Suc" + str(num))

def main ():
    print 1
    unifo = []
    url = 'http://www.zuihaodaxue.cn/shengyuanzhiliangpaiming2016.html'
    html = getHTMLText(url)
    fillUnivList(unifo, html)
    printUnivList(unifo, 20) #20

main()




