#!/usr/bin/env python3

import cgi
import os
import html
#import socket
import json
form=cgi.FieldStorage()
print("Content-type:text/html\n\n")

print("<html><body>")


#http://127.0.0.1/addaddress.py?add=add&camera=jerry&address=leep1995%40gmail.com&passw=sad&sens=7
add=form["add"].value
passw=form["passw"].value
address=form["address"].value
camera=form["camera"].value
try:
	sens=float(form["sens"].value)
except:
	sens=None

#read json, get appropriate ip

#append this data to the list,in main directory for script to execute

#s=socket.socket(

if add and camera and sens:
	os.chdir("..")
	f=open("reqs.txt","a")
	f.write(add+","+address+","+passw+","+camera+","+str(sens)+"\n")
	f.close()
else:
	print("incorrect entry")
print("<p> Sent.</p><br><a href='index.html'>Click here</a></body></html>")
