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

def listInt_toString(liste_entiers):
    # Convertir chaque entier en une liste de bytes
    liste_bytes = [list(i.to_bytes((i.bit_length() + 7) // 8, 'big') or b'\0') for i in liste_entiers]

    # Décoder chaque liste de bytes en un caractère
    message = ''.join(bytes(b).decode('utf-8') for b in liste_bytes)

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

def vignere(msg, key):
    key = str(key)
    result = msg[:]
    key_length = len(key)
    counter = 0
    counter2 = 0

    while counter <= len(result) - 1:
        unit = [result[counter]]
        result[counter] = shifter(unit, key[counter2])[0]
        counter += 1
        counter2 = (counter2 + 1) % key_length

    return result

def devignere(msg, key):
    result = msg[:]
    key_length = len(key)
    counter = 0
    counter2 = 0

    while counter <= len(result) - 1:
        unit = [result[counter]]
        result[counter] = deshifter(unit, key[counter2])[0]
        counter += 1
        counter2 = (counter2 + 1) % key_length

    return result







# a0 = [1, 2, 3, 4]
# b = [9, 3]
# c = vignere(a0, b)
# print('Encrypted:', c)
# d = devignere(c, b)
# print('Decrypted:', d)

#test = "j'aime le Chocolat ç `ñ"

#print(test)
# # Transformer le texte en une liste de lettre convertie en utf8 (entier) stocké dans une liste d'entier
#returnresult = string_toListInt(test)

#print(returnresult)
# # shifter de 1 chaque entier de la liste
# print(shifter(returnresult,1))
# # transformer chaque entier en un chiffre binaire de 4 bytes et en ajoutant au début " bytes correspondants au nombre de caractères envoyés
# print(encoding(shifter(returnresult,1)))
# #décoder la suite de binaire en une liste d'entier
# print(decoding(encoding(shifter(returnresult,1))))
# #fonction qui enlève le shift sur tous les membres de liste d'entier
# print(deshifter(decoding(encoding(shifter(returnresult,1))),1))
# #fonction qui converti la liste d'entier en un string
# print(listInt_toString(deshifter(decoding(encoding(shifter(returnresult,1))),1)))

# print("----------------------------------------------------------------")

# print(test)
# print(returnresult)
# # xor de 4 chaque entier de la liste
# print(xor(returnresult,4))
# # transformer chaque entier en un chiffre binaire de 4 bytes et en ajoutant au début " bytes correspondants au nombre de caractères envoyés
# print(encoding(xor(returnresult,4)))
# #décoder la suite de binaire en une liste d'entier
# print(decoding(encoding(xor(returnresult,4))))
# #fonction qui enlève le xor sur tous les membres de liste d'entier
# print(xor(decoding(encoding(xor(returnresult,4))),4))
# #fonction qui converti la liste d'entier en un string
# print(listInt_toString(xor(decoding(encoding(xor(returnresult,4))),4)))
