#!/usr/bin/env python3
import os
import cgi
import html
#import socket
import json

print("Content-type: text/html\n\n")
print("<html> <body>Helloworld")

form=cgi.FieldStorage()
print(form)
try:
	addorremove=form["add"].value #watch this
	passw=form["passw"].value
	addr=form["address"].value
	camchoice=form["camera"].value
	sens=form["sens"].value
#read json, get appropriate ip
except:
	print ("INVALID FORM")
	raise

#append this data to the list,in main directory for script to execute

#s=socket.socket(
if camchoice and addorremove:
	os.chdir("..")
	f=open("reqs.txt","a")

	f.write(addorremove+","+addr+","+passw+","+camchoice+","+sens+"\n")

	f.close()


