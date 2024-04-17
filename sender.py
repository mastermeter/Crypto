import socket
import mainFunctions
import rsaFunctions


HOST = "vlbelintrocrypto.hevs.ch"
port = 6000
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

def receive_message():
    rcv_msg = sock.recv(65536) # 64Ko
    rcv_msg = rcv_msg.replace(b'\0',b'')
    rcv_msg = rcv_msg.decode('utf-8')
    rcv_msg = rcv_msg[5:]

    print(rcv_msg)

def send_message():
    #envoi
    msg = ""
    txt_encoded = ""
    
    key = "ISC"
    msg_type = input("Entrez un type de message : (t,i,s) : ")

    if msg_type != "t" and msg_type != "i" and msg_type != "s":
        print("Type de message non reconnu")
        msg_type = input("Entrez un type de message : (t,i,s) : ")
    msg = str.encode(key + msg_type)
    txt = input("Entrez votre texte : ")

    #Connaitre type d'encodage
    encoding_type = input("Entrez un type d'encodage : (none, shift, xor, rsa) : ")
    if encoding_type == "none":
        txt_encoded = mainFunctions.string_toListInt(txt)

    elif encoding_type == "shift":
        shift = int(input("Entrez un nombre pour le décalage : "))
    
        txt_encoded = mainFunctions.string_toListInt(txt)
        txt_encoded = mainFunctions.shifter(txt_encoded,shift)

    elif encoding_type == "xor":
        nb = int(input("Entrez un nombre pour le xor : "))
        #msg = mainFunctions.string_toListInt(msg)
        #msg = mainFunctions.xor(msg,nb)
    else:
        print("Type d'encodage non reconnu")

    # adaptation nombre de caractère
    longueur_txt = len(txt)
    nb_char = longueur_txt.to_bytes(2,"big")

    txt_encoded = mainFunctions.listInt_toString(txt_encoded)
    
    final_text = mainFunctions.word_to_bytes(txt_encoded)
    
    msg_final = msg + nb_char + final_text



    
    sock.send(msg_final)



sock.connect((HOST,port))
cont = True


send_message

while cont :
    send_message()
    receive_message()
    #print("Send a new message ?")
    #txt2 = input("y/n : ")
    # if txt2 == "n":
    #     cont = False
    #     print("End of the communication")
    
sock.close()