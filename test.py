rcv_msg1 = "ñ"
rcv_msg2 = rcv_msg1.encode('utf-8')
binary_string = ''.join(format(byte, '08b') for byte in rcv_msg2)

# Remplissage avec des zéros à gauche si nécessaire
while len(binary_string) < 32:
    binary_string = '0' + binary_string

# Assurez-vous que le résultat a exactement 32 bits
binary_string = binary_string[-32:]
print(binary_string)

def convert_to_4bytes_binary(text):
    result = []
    for char in text:
        binary_char = bin(ord(char))[2:].zfill(32)  # Convertir le caractère en binaire sur 32 bits
        binary_char = int(binary_char,2)
        result.append(binary_char)
    return result

phrase = ("Hello world ç")
binary_list = convert_to_4bytes_binary(phrase)

print(binary_list)




