#!/usr/bin/env python3

import cgi
import html
#import socket
import json
form=cgi.FieldStorage()

passw=form.getone("pass")
addr=form.getone("addr")
choice=form.getone("camera")
#read json, get appropriate ip

#append this data to the list,in main directory for script to execute

#s=socket.socket(
