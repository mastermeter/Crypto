#considering txt which is string and a key which is a string
def vigenere(listInt,key):
    print(listInt)
    print(key)
    keyInList = []
    transfomTxtInList = []
    while len(listInt)>len(key):
        key+=key
    print(listInt)
    print(key)
    for i in range(len(listInt)):
        keyInList.append(int.from_bytes(key[i].encode('utf-8')))
        transfomTxtInList.append(listInt[i]+keyInList[i])
    print(keyInList)
    print(listInt)
    print(transfomTxtInList)
    return transfomTxtInList