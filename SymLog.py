#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests, json
import re


myList = []          ## ¿ÕÁÐ±í

fileold = open("E:\data_set\data_set", "r")
configfile_list = fileold.readlines()
fileold.close()

totalIndex = configfile_list.__len__()-1

def SynText( Line ):
	listAdd = ['', '', '', '','']
	lineAllArray = Line.split(' ')
	listAdd[0] = lineAllArray[3]
	listAdd[1] = lineAllArray[2]

	lineArray = Line.split(':')
	lineLength = lineArray.__len__()

	if lineLength > 1:
		listAdd[2] = lineArray[1]
		# matchObj = re.match( r'\(.*\)', lineLength[0], re.M|re.I)
		# if matchObj:
		# 	matchBody=matchObj.group()
		# 	matchNumObj = re.match( r'\[.*\]', matchBody, re.M|re.I)

		# 	listAdd[3] = matchBody.group()
		# 	if matchNumObj:
		# 		listAdd[4] = matchNumObj.group()
		# 	else:
		# 		listAdd[4] = ""
		# else:
		# 	listAdd[3] = ""
		# 	listAdd[4] = ""
	# else:
	# 	lineArray = Line.split('-')
		#listAdd[2]  = lineArray[3]

	return listAdd

for i in range(totalIndex):
	nextIndex = int(i)+1
	if nextIndex > totalIndex:
		nextIndex=totalIndex

	lineBody = configfile_list[i]
	atchObj = re.match( r'May.*', lineBody, re.M|re.I)
	if atchObj:
		nextBody=configfile_list[nextIndex]
		matchObj = re.match( r'May.*', nextBody, re.M|re.I)
		if matchObj:
			myList.append(SynText(lineBody))
		else:
			lineBody = lineBody + nextBody

print (myList)
ticketNo = input()