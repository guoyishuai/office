# -*- coding:utf-8 -*-
import requests
import os

url = "https://img14.360buyimg.com/n0/jfs/t19675/80/490597782/206146/44220659/5a8fcf76N4d1f88a3.jpg"
root = "D:/123/"
path = root + url.split('/')[-1]

try:
    if not os.path.exists(root):
        os.mkdir(root)
#    if os.path.exists(root):
    if not os.path.exists(path):
        r = requests.get(url)
        print 111
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print ("文件保存成功")
    else:
        print("文件已存在")
except:
    print "爬取失败"

