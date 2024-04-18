#considering txt which is string and a key which is a string
def vigenere(txt,key):
    txtInList = []
    keyInList = []
    transfomTxtInList = []
    while len(txt)>len(key):
        key+=key
        print(key)
        print(txt)
    for i in range(len(txt)):
        txtInList.append(int.from_bytes(txt[i].encode('utf-8')))
        keyInList.append(int.from_bytes(key[i].encode('utf-8')))
        transfomTxtInList.append(txtInList[i]+keyInList[i])
    return transfomTxtInList

    
vigenere("Salut à tous les amis, comment ça va ?","afhjgvkfj")


