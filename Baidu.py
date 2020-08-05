#!/usr/bin/python
# -*- coding: UTF-8 -*-

body = input("中文:")

import random
import hashlib
import requests, json

random = random.randint(0,999)

appid="20200331000409238"
pwd = "AtiKZkcz4apIxCsdVklr"
sign = appid + body + random + pwd
m= hashlib.md5(s.encode())
print(m.hexdigest())


github_url="http://api.fanyi.baidu.com/api/trans/vip/translate?q="+body+"&from=zn&to=en&appid="+appid+"&salt="+random+"&sign=" + m.hexdigest()

#r = requests.post(github_url)
#print (r.text)

input(":")