import socket

HOST = "vlbelintrocrypto.hevs.ch"
port = 6000
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Envoi
key = "ISC"
msg_type = input("Entrez un type de message : (t,i,s) : ")
msg = str.encode(key + msg_type)

# adaptation nombre de caractère
txt = input("Entrez votre texte : ")
longueur_txt = len(txt)
nb_char = longueur_txt.to_bytes(2,"big")
txt_encoded = ""
null = '\0'
for i in range(len(txt)):
    txt_encoded += 3*null + txt[i]  
txt_encoded = str.encode(txt_encoded, 'utf-8')
msg_final = msg + nb_char + txt_encoded

sock.connect((HOST,port))
sock.send(msg_final)
while True :
    rcv_msg = sock.recv(65536)
    print(str.encode(rcv_msg, 'utf-8'))
        
 