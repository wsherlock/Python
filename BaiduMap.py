#!/usr/bin/python
# -*- coding: UTF-8 -*-

city = input("城市:")
area = input("地区:")

import requests, json

github_url="https://api.map.baidu.com/place/v2/suggestion?query="+ city + "&region="+ area + "&city_limit=true&output=json&ak=O6MAZ9kjxMs3eCHLTZ66FSwz"

r = requests.post(github_url)
rs = json.loads(r.text)

dataList = rs.get('result')

for x in dataList:
    name = x['name']
    if ('location' in x) :
        lat = x['location']['lat']
        lng = x['location']['lng']
    else:
        lat = "Unkown"
        lng = "Unkown"
    print ("name:%s" % name,"lat: %s" % lat,"lng:%s" % lng)

input("")