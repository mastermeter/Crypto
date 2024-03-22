def modulo_exponentiation(a, e, n):
    result = 1
    power_of_a = a % n  # Initialise la puissance de 'a' à 'a % n'

    # Convertir l'exposant en binaire
    binary_exponent = bin(e)[2:]  # Ignorer le préfixe '0b'

    # Parcourir chaque bit de l'exposant
    for bit in binary_exponent[::-1]:  # Inverser la chaîne binaire pour commencer par les bits de poids faible
        if bit == '1':
            result = (result * power_of_a) % n
        power_of_a = (power_of_a * power_of_a) % n  # Calculer la puissance de la puissance de 2 suivante modulo 'n'

    return result

# Exemple d'utilisation
a = 34
e = 13
n = 2 ** 32
k = modulo_exponentiation(a, e, n)
print(k)