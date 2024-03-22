def gcd(a, b):
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i

# Algorithme d'Euclide étendu
## y = b, pas négatif
def extended_gcd(e, k):
    if e == 0:
        return k, 0, 1
    else:
        gcd, x, y = extended_gcd(k % e, e)
        x, y = y - (k // e) * x, x
        return gcd, x % k, y  # Utilisez le modulo k pour garantir que x est positif


def isPrime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def isCoprime(a, b):
    if gcd(a,b) == 1:
        return True
    
    return False

def coprimeWith(a):
    for i in range(2, a):
        if isCoprime(a, i):
            if i < a:
                return i

def generate_key(p,q):
    while(isPrime(p) == True and isPrime(q) == True and p*q < 2**32):
        n = p*q
        k = (p-1)*(q-1)
        e = coprimeWith(k) 
        l, d, b = extended_gcd(e,k)
        print(n, k,  e,  d,  b,  l) 
        return n, e, d

# méthode optimisée pour encrypt et decrypt
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

def encryptKey(message, e, n):
    return modulo_exponentiation(message, e, n)

def decryptKey(hiddenMess, d, n):
    return modulo_exponentiation(hiddenMess, d, n)  
     

n, e, d = generate_key(211, 541)


lol = encryptKey(666, e, n)

print(encryptKey(666, e, n))
print(decryptKey(lol, d, n))