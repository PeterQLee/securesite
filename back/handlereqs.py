import socket
import json
import threading
import time
#this program handles requests to be added to the system
#uses port 6000

#hands out ports above 6100
#additionally writes JSON data
class HandleReqs:
            
    clientdict={}
    adddict={}
    tdict={}
    def __init__(self):
        self.s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        self.s.bind(("",6000))
        self.s.listen(5)
        self.addsock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.addsock.bind(("",6001))
        self.addsock.listen(5)

    def handlealert(self,client):
        try:
            while True:
                self.alert=client.recv(128)
        #print alert to webdata+time +image if we're doing that
        #f=open("securesite/log","a")
        #f.write(alert.decode("utf-8"))
        #f.close()
        except:
            print("stuff stopped")
    def positiveret(self,val):
        if val.decode()=='1':return True
        return False 
    def addemail(self,clientname):
        print ("sbemail")
        while True:
            f=open("reqs.txt","r")
            
            j=f.readline()
            while j!="":
            #read file and spit 
                ops=j.split(",")
                addorremove=ops[0]
                emailaddr=ops[1]
                passw=ops[2]
                camchoice=ops[3]
                sens=ops[4][:len(ops[4])]
            
                print("Send "+str(ops))
                if camchoice not in self.adddict:
                    j=f.readline()
                    continue
                print(1)
                self.adddict[camchoice].send(bytes(addorremove,"utf-8"))
                if  not self.positiveret(self.adddict[camchoice].recv(128)): #check for positive
                    j=f.readline()
                    continue
                print(2)
                self.adddict[camchoice].send(bytes(passw,"utf-8"))

                if addorremove=="halt" or addorremove=="resume":continue #if switch, just stop
                
                if not self.positiveret(self.adddict[camchoice].recv(128)): #check for positive
                    j=f.readline()
                    continue
                print(3)
                self.adddict[camchoice].send(bytes(emailaddr,"utf-8"))
                if not self.positiveret(self.adddict[camchoice].recv(128)): #check for positive
                    j=f.readline()
                    continue
                print(4)
                self.adddict[camchoice].send(bytes(sens,"utf-8"))
                j=f.readline()
                print("done")
            f.close()
            f=open("reqs.txt","w")
            f.close()
           
            time.sleep(5)
            
            

    def writecameras(self,camer):
        f=open("Site/cameras.json","r")
        buf=f.read()
        if buf=="":
            df=[]
        else:
            df= json.loads(buf)
        if camer in df:
            f.close()
            return
        else:
        
            df.append(camer)
            f.close()
            f=open("Site/cameras.json","w")
            f.write(json.dumps(df))
            f.close()
    def lobby(self):
        print("started lobby")
        while True:
            try:
                (client,addr)=self.s.accept()
                buf=client.recv(128)
                nm=buf.decode()#decode to string
                if nm in self.clientdict: #clean previous socks
                    self.clientdict[nm].close()
                    self.adddict[nm].close()
                self.writecameras(nm)
                self.clientdict[nm]=client

                (add,addr)=self.addsock.accept()
                print("accepted!")
                self.adddict[nm]=add
                print ("handled "+nm)
                threading.Thread(target=self.handlealert,args=(self.clientdict[nm],)).start()
                threading.Thread(target=self.addemail,args=(self.adddict[nm],)).start()
                print("threads started")
            except:
                self.addsock.close()
                self.s.close()
                raise
    #tdict{nm}
    #spawn new thread, handlereq
            
    
    
    
    
    """
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
    """
M=HandleReqs()
M.lobby()
