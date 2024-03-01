import socket

HOST = "vlbelintrocrypto.hevs.ch"
port = 6000
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#functions
def receive_message():
    rcv_msg = sock.recv(65536) # 64Ko
    rcv_msg = rcv_msg.decode('utf-8')
    rcv_msg = rcv_msg[4:]
    print(rcv_msg)

sock.connect((HOST,port))
#sock.send(msg_final)
while True :
    receive_message()
        
 

