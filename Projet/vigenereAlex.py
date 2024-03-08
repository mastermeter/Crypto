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
        transfomTxtInList[i]=transfomTxtInList[i].to_bytes(4,byteorder='big')
        transfomTxtInList[i]=transfomTxtInList[i].decode('utf-8')
    print(txtInList)
    print(keyInList)
    print(transfomTxtInList)

    
vigenere("Salut à tous les amis, comment ça va ?","afhjgvkfj")


