# -*- coding:utf-8 -*-
from urllib import urlopen

def login():
	postdata = "DDDDD=shixi&upass=shixi&0MKKey=µÇÂ¼ÏµÍ³+Login";
	postdata = postdata.encode('utf-8');
	urlopen("http://172.16.0.252", postdata);

url = None
try:
	url = urlopen('http://www.baidu.com')
	s= url.getcode()
except:
	print("The computer is offline, will auto login")
 
