#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests, json
from xml.dom.minidom import parse
import xml.dom.minidom

while 1>0:
    ticketNo = input("TicketNo:")
    github_url="http://agibe.travelsky.com/ota/xml/AirTicketRet"
    data = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><TES_AirTicketRetRQ><POS><Source PseudoCityCode=\"BJS723\" /></POS><TicketNumber>%s</TicketNumber></TES_AirTicketRetRQ>" % ticketNo
    headers = \
        {
            "Authorization": "Basic emhqeDpld2ljODE5MA=="
        }

    r = requests.post(github_url,headers=headers,data=data)

    DOMTree = xml.dom.minidom.parseString(r.text)

    collection = DOMTree.documentElement

    Errors = collection.getElementsByTagName("Error")
    if Errors.length >0:
        for Error in Errors:
            if Error.hasAttribute("ShortTextZH"):
                print ("Error : %s" % Error.getAttribute("ShortTextZH"))
    else:
        if collection.hasAttribute("FlightSegments"):
            print ("Root element : %s" % collection.getAttribute("FlightSegments"))

        FlightSegments = collection.getElementsByTagName("FlightSegment")

        for FlightSegment in FlightSegments:
            if FlightSegment.hasAttribute("TicketStatus"):
                print ("客票状态: %s" % FlightSegment.getAttribute("TicketStatus"))
        
        DepartureAirport = FlightSegment.getElementsByTagName('DepartureAirport')[0]
        print ("出发机场: %s" % DepartureAirport.getAttribute("LocationCode"))

        ArrivalAirport = FlightSegment.getElementsByTagName('ArrivalAirport')[0]
        print ("到达机场: %s" % ArrivalAirport.getAttribute("LocationCode"))

    ticketNo = input("TicketNo:")
