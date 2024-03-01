def btoint(message):
    message = message.encode('utf-8')
    liste_entiers = [b for b in message]
    for element in liste_entiers:
        print(element)
    return liste_entiers

def encoding(liste_entiers):
    binaires = [format(elem,'32b') for elem in liste_entiers]
    result = ''.join(binaires)


print(encoding(btoint("Hello world ç")))

