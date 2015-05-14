#imports
import socket
from threading import *
import time
import os.path


#helper functions
def writeLog(cameraName):
    path = 'logs/' + cameraName+'Logs.txt'

    log_entry = (time.strftime("%d/%m/%Y") + "\t"
    + time.strftime("%H:%M:%S")
    + "\tMotion Detected!"+"<br>\n")

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
        num_lines = sum(1 for line in open('logs/' + cameraName+'Logs.txt'))
        print(num_lines)



serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#use IP of device
host = "127.0.0.1"
port = 8000
print (host)
print (port)
serversocket.bind((host, port))
serversocket.listen(5)
print ('server started and listening')
while 1:
    clientsocket, address = serversocket.accept()
    #client(clientsocket, 
    clientData = clientsocket.recv(1024).decode()
    print(clientData)
    writeLog(clientData)
    
        #To do, write to file
    
    clientsocket.close()
