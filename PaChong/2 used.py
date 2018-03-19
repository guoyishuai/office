# -*- coding: utf-8 -*-
import  requests

def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
#        r.encoding =r.apparent_encoding
        r.encoding= "utf-8"
        print r.text
        return r.text

    except:
        return "产生异常"

url = "http://tieba.baidu.com/f?kw=%D3%C0%D2%B9%BE%FD%CD%F5&fr=ala0&loc=rec"
#if __name__ == "__main__":
getHTMLText(url)

#print(getHTMLText(url))


#getHTMLText("http://www.baidu.com")