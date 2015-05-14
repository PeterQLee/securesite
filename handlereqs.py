import socket
import json
import threading
import time
import os
#this program handles requests to be added to the system
#uses port 6000

#hands out ports above 6100
#additionally writes JSON data
class HandleReqs:
            
    clientdict={}
    adddict={}
    tdict={}
    names=[]
    def __init__(self):
        self.s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        self.s.bind(("",6000))
        self.s.listen(5)
        self.addsock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.addsock.bind(("",6001))
        self.addsock.listen(5)

    def handlealert(self,client,nm):
        try:
            while True:
                alert=client.recv(128)
                self.writeLog(nm)
        #print alert to webdata+time +image if we're doing that
        #f=open("securesite/log","a")
        #f.write(alert.decode("utf-8"))
        #f.close()
        except:
            print("stuff stopped")
    def writeLog(self,cameraName,message="\tMotion Detected!"):
        path = 'Site/logs/' + cameraName+'Logs.txt'

        log_entry = (time.strftime("%d/%m/%Y") + "\t"
                     + time.strftime("%H:%M:%S")
                     + message+"<br>\n")

        if not os.path.isfile(path):
            print('ahh shit')
            text_file = open(path, 'a')
            text_file.write(log_entry)
            text_file.close()
        else:   
            with open(path, 'r') as file:
        # read a list of lines into data
                data = file.readlines()

            print (data)
            data.insert(0,log_entry)
    # now change the 2nd line, note that you have to add a newline
        #data[1] = 'Mage\n'

    # and write everything back
            if len(data) > 50:
                with open(path, 'w') as file:
                    file.writelines( data[:50] )
            else:
                with open(path, 'w') as file:
                    file.writelines( data )
            num_lines = sum(1 for line in open('Site/logs/' + cameraName+'Logs.txt'))
            print(num_lines)

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
        print("start?")
        f=open("Site/cameras.json","r")
        buf=f.read()
        if buf=="":
            df=[]
        else:
            df= json.loads(buf)
        if camer in df:
            f.close()
            
        else:
        
            df.append(camer)
            f.close()
            f=open("Site/cameras.json","w")
            f.write(json.dumps(df))
            f.close()
        #write html files
        f=open("template.html",'r')
        out=os.open("Site/"+camer+".html",os.O_WRONLY|os.O_CREAT|os.O_TRUNC,int("0777",8))
        fout=os.fdopen(out,"w")
        fout.write(f.read().replace("%s",camer))
        fout.close()
        f.close()
        #write js files
        f=open("template.js","r")
        out=os.open("Site/js/"+camer+".js",os.O_WRONLY|os.O_CREAT|os.O_TRUNC,int("0777",8))
        fout=os.fdopen(out,"w")
        fout.write(f.read().replace("%s",camer))
        fout.close()
        f.close()
        #start off the log file
        
        path = 'Site/logs/' + camer+'Logs.txt'

        #prepare log
        out=os.open(path,os.O_WRONLY|os.O_CREAT,int("0777",8))
        self.writeLog(camer,"\tConnection Established!")
        print("DONE")
        
    def lobby(self):
        print("started lobby")
        while True:
            try:
                (client,addr)=self.s.accept()
                buf=client.recv(128)
                nm=buf.decode()#decode to string
                if nm=="index":continue #can't have anyone named index
                if nm in self.clientdict: #clean previous socks
                    self.clientdict[nm].close()
                    self.adddict[nm].close()
                self.writecameras(nm)
                self.clientdict[nm]=client

                (add,addr)=self.addsock.accept()
                print("accepted!")
                self.adddict[nm]=add
                print ("handled "+nm)
                names.append(nm)
                threading.Thread(target=self.handlealert,args=(self.clientdict[nm],nm)).start()
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
M.writecameras("jon")
#M.lobby()
