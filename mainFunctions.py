def string_toListInt(message):
    liste_bytes = [list(char.encode('utf-8')) for char in message]

    # Convertir chaque liste de bytes en un entier
    liste_entiers = [int.from_bytes(bytes(b), 'big') for b in liste_bytes]

    return liste_entiers

def encoding(liste_entiers):
    binary_list = [format(elem, '032b') for elem in liste_entiers]
    # Ajouter la représentation binaire de la taille de la liste
    size_binary = format(len(liste_entiers), '016b')  # 2 bytes pour la taille
    binary_list = [size_binary] + binary_list
    return ''.join(binary_list)


def decoding(binary_string):
    # Extraire la taille de la liste d'entiers
    size_binary = binary_string[:16]
    size = int(size_binary, 2)

    # Extraire les entiers de la chaîne binaire
    integers = []
    for i in range(16, len(binary_string), 32):
        integer_binary = binary_string[i:i + 32]
        integer = int(integer_binary, 2)
        integers.append(integer)

    # Vérifier si la taille correspond au nombre d'entiers
    if size != len(integers):
        raise ValueError("Taille incorrecte de la liste d'entiers")

    return integers

def word_to_bytes(word):
    # Convert each character to bytes, pad to 4 bytes if necessary
    byte_string = b''.join(b'\x00' * (4 - len(char.encode('utf-8'))) + char.encode('utf-8') for char in word)
    return byte_string

# def listInt_toString(liste_entiers):
#      # Convertir chaque entier en une liste de bytes
#     liste_bytes = [list(i.to_bytes((i.bit_length() + 7) // 8, 'big') or b'\0') for i in liste_entiers]

#      # Décoder chaque liste de bytes en un caractère
#     message = ''.join(bytes(b).decode('utf-16') for b in liste_bytes)

#     return message
   
def listInt_toString(liste_entiers):
     # Convertir chaque entier en un caractère
    message = ''.join(chr(i) for i in liste_entiers)

    return message

def shifter(msg,shift) :
    #Ajouter l'entier à chaque élément de la liste
    resultats = [elem + shift for elem in msg]
    return resultats


def deshifter(msg,deshift) :
    # Soustraire l'entier à chaque élément de la liste
    resultats = [elem - deshift for elem in msg]
    return resultats

def xor(msg,nb) :
    resultats = [elem ^ nb for elem in msg]
    return resultats

def vigenere(listInt,key):
    keyInList = []
    transfomTxtInList = []
    while len(listInt)>len(key):
        key+=key
        print(key)
        print(listInt)
    for i in range(len(listInt)):
        keyInList.append(int.from_bytes(key[i].encode('utf-8')))
        transfomTxtInList.append(listInt[i]+keyInList[i])
    return transfomTxtInList

def devigenere(msg, key):
    result = []
    finalkey = key
    while len(finalkey)<len(msg):
        finalkey+=key
    for i in range(len(msg)):
        result = msg[i]-finalkey[i]
    return result


print(encoding([34646]))