import requests

r = requests.get('https://t.bilibili.com/')

r.encoding = 'utf-8'
print r.text