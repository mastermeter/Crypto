#transforms each character in a bytes chain in an integer
def btoint(message):
    message = message.encode('utf-8')
    liste_entiers = [b for b in message]

    return liste_entiers

def encoding(liste_entiers):
    chain = b''.join([bytes([elem]) for elem in liste_entiers])
    print(chain)


print(encoding(btoint("Hello world ç")))

