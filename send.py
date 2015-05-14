import socket

#sends an alert to the server using the device name
def alert_Server():
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host ="127.0.0.1"
    port =8000
    s.connect((host,port))
    #enter name of device
    deviceName = "MacCam"
    s.send(deviceName.encode())
    s.close()

#test Code
while 1:
    alert_Server()
    #debug code
    r=input('enter')