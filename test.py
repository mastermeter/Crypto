


def string_toListInt(message):
    message = message.encode('utf-8')
    liste_entiers = [b for b in message]

    return liste_entiers

# def encoding(liste_entiers):
#     binaires = [format(elem,'32b') for elem in liste_entiers]
#     result = "".join(binaires)
#     return result

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

def listInt_toString(entiers):
    # Convertir chaque entier en caractère en utilisant UTF-8
    message_bytes = bytes(entiers)
    decoded_string = message_bytes.decode('utf-8')
    return decoded_string

def shifter(msg,shift) :
    # Ajouter l'entier à chaque élément de la liste
    resultats = [elem + shift for elem in msg]
    return resultats


def deshifter(msg,deshift) :
    # Soustraire l'entier à chaque élément de la liste
    resultats = [elem - deshift for elem in msg]
    return resultats


test = "j'aime le Chocolat"

print(test)
# Transformer le texte en une liste de lettre convertie en utf8 (entier) stocké dans une liste d'entier
returnresult = string_toListInt(test)

print(returnresult)
# shifter de 1 chaque entier de la liste
print(shifter(returnresult,1))
# transformer chaque entier en un chiffre binaire de 4 bytes et en ajoutant au début " bytes correspondants au nombre de caractères envoyés
print(encoding(shifter(returnresult,1)))
#décoder la suite de binaire en une liste d'entier
print(decoding(encoding(shifter(returnresult,1))))
#fonction qui enlève le shift sur tous les membres de liste d'entier
print(deshifter(decoding(encoding(shifter(returnresult,1))),1))
#fonction qui converti la liste d'entier en un string
print(listInt_toString(deshifter(decoding(encoding(shifter(returnresult,1))),1)))