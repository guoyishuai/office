# -*- coding:utf-8 -*-
import requests
import re

def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        #print r.text
        return r.text
    except:
        return ""

def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
        print 1
        print plt
        print 2
        print tlt
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price, title])
    except:
        print("")

def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print tplt.format("xuhao", "jiage", "mingcheng")
    count = 0
    for g in ilt:
        count +=1
        print tplt.format(count, g[0], g[1])

def main():
    goods = "shubao"
    depth = 2
    start_url = "https://s.taobao.com/search?q="+ goods
    infoList = []
    for i in range (depth):
        try:
            url = start_url + "&s=" + str(44*i)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            continue
    printGoodsList(infoList)

main()