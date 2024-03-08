import socket
import mainFunctions

HOST = "vlbelintrocrypto.hevs.ch"
port = 6000
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#functions
def receive_message():
    rcv_msg = sock.recv(65536) # 64Ko
    rcv_msg = rcv_msg.replace(b'\0',b'')
    rcv_msg = rcv_msg.decode('utf-8')
    rcv_msg = rcv_msg[5:]
    print(rcv_msg)

sock.connect((HOST,port))

while True :
    receive_message()
   
        
 

