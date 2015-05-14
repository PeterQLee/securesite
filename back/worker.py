import socket

#note, we will need a file with all ports and addresses
#this program monitors and sends added users to appropriate nodes

while True:
    f=open("reqs.txt")
    d=open("cameras.txt")
    dat=d.read()
    data=s.replace("'"."\"")
    data=json.loads(data)
    l=f.readLine()
    while l!="":
        ops=l.split(",")
        addorremove=ops[0]
        emailaddr=ops[1]
        passw=ops[2]
        camchoice=ops[3]
