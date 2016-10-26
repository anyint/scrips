#!/usr/bin/env python
#coding:utf-8
import urllib2
req = urllib2.Request('http://www.baidu.com')
try:
	url = urllib2.urlopen(req)
except urllib2.URLError,e:
	print e.reason
	print e.reason[0]
	print e.reason[1]
print("end")	
 
