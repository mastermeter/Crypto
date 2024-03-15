import socket
import mainFunctions


HOST = "vlbelintrocrypto.hevs.ch"
port = 6000
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

def send_message():
    #envoi
    msg = ""
    txt_encoded = ""
    
    key = "ISC"
    msg_type = input("Entrez un type de message : (t,i,s) : ")
    msg = str.encode(key + msg_type)
    
    txt = input("Entrez votre texte : ")

    #Connaitre type d'encodage
    encoding_type = input("Entrez un type d'encodage : (shift, xor) : ")
    if encoding_type == "shift":
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

while cont :
    send_message()
    
    print("Send a new message ?")
    txt2 = input("y/n : ")
    if txt2 == "n":
        cont = False
        print("End of the communication")
    
sock.close()