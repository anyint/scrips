#!/usr/bin/env python3
#coding:utf-8

import os
import urllib.request
def login():
	postdata = "DDDDD=shixi&upass=shixi&0MKKey=µÇÂ¼ÏµÍ³+Login";
	postdata = postdata.encode('utf-8');
	urllib.request.urlopen("http://172.16.0.252", postdata);
	return
return1=os.system('ping 8.8.8.8 -c 2')
#return1=os.system('ping 192.168.88.1 -c 2')
if return1:
    print("The computer is offline, will auto login")
    login()
else:
    print("The internet is ok")
