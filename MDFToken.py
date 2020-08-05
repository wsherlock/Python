#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests, json
from xml.dom.minidom import parse
import xml.dom.minidom

while 1>0:
    url = "https://test.cwtwebservices.com/getAccessToken"
    payload = {"client_id":"esg.travelorder.yeego","client_secret":"uPC1ioNp1aiwoyYwV2Zt1bLc4wINrLeaVXGT73rzWDZUz9EzdQQf7mD4zIWXgMzO","grant_type":"client_credentials"}
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host':'test.cwtwebservices.com',
        'Content-Length':'140',
        'Connection': 'Keep-Alive'
    }
    response = requests.post(url, headers=headers, data=payload)
    print(response.text)
    ticketNo = input()