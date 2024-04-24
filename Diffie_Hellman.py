from math import pow

def eratosthene(Limite):
    # Création et initialisation du tableau de booléens
    TableauBoolean = [True] * (Limite + 1)
    primes = []

    # Mettre à Faux les cases d'indice pair > 2
    for i in range(4, Limite + 1, 2):
        TableauBoolean[i] = False

    # Marquer 1 comme non-premier
    TableauBoolean[1] = False

    i = 3
    while i * i <= Limite:
        if TableauBoolean[i]:
            # Marquer comme non-premiers tous les multiples de i
            for j in range(i * i, Limite + 1, 2 * i):
                TableauBoolean[j] = False
        i += 1

    # Ajouter les nombres premiers à la liste
    for i in range(2, Limite + 1):
        if TableauBoolean[i]:
            primes.append(i)

    return primes

def is_prime(n, i=2):
    # Base cases
    if n == 0 or n == 1:
        return False
    if n == 2:
        return True

    # Simpler but less effective
    if i == n:
        return True

    # If can be divided by i, not prime
    if n % i == 0:
        return False

    # Check for next divisor
    return is_prime(n, i + 1)

def is_prime_factors(n):
    list_nb_primes = eratosthene(n)
    result = []
    test = n
    position_liste = 0

    while test != 1 and position_liste < len(list_nb_primes):
        nb_premier = list_nb_primes[position_liste]

        # Tant que le nombre est divisible par le nombre premier actuel
        while test % nb_premier == 0:
            # Ajouter ce nombre premier à la liste des co-facteurs premiers
            result.append(nb_premier)
            # Diviser le nombre par le nombre premier
            test //= nb_premier

        # Passer au prochain nombre premier dans la liste
        position_liste += 1

    # Ajouter le dernier co-facteur premier s'il reste un nombre non divisé
    if test != 1:
        result.append(test)

    return result

def test_non_congruence(list_co_fact_prime, g, n):
    position = 0
    n_moins_1 = n - 1
    result = False
    faux = True

    while position < len(list_co_fact_prime) and faux:
        a = n_moins_1 // list_co_fact_prime[position]

        if (g ** a) % n != 1:
            position += 1
            result = True
        else:
            result = False
            faux = False

    return result

def generator(k):
    k_moins_1 = k - 1
    result = []

    liste_nb_premiers_jusq_n_moins_1 = eratosthene(k_moins_1)
    liste_co_facteurs_de_n_moins_1 = is_prime_factors(k_moins_1)

    for g in range(1, k_moins_1 + 1):
        test_de_g = test_non_congruence(liste_co_facteurs_de_n_moins_1, g, k)
        if test_de_g:
            result.append(g)

    return result

nb = 653
#print(eratosthene(800))
#print(generator(nb))

def is_primitive_roots(modulo, roots):
    # Calcul de l'ordre du groupe multiplicatif modulo n
    def euler_phi(n):
        result = n
        i = 2
        num = n  # Copie de n pour effectuer les opérations de division
        while i * i <= n:
            if num % i == 0:
                while num % i == 0:
                    num //= i  # Division et assignation
                result -= result // i
            i += 1
        if num > 1:
            result -= result // num
        return result

    # Vérification si chaque nombre de l'array est une racine primitive modulo n
    return all(euler_phi(modulo) == modulo - 1 for root in roots)

# Exemple d'utilisation
print(is_primitive_roots(nb, generator(nb)))

# A et B choisissent un p (nombre premier pris au hasard (p < 256^4) )
p = 347
#Modular word = p
# A et B choisissent un g (grâce à la fonction generator, qui retourne une liste de g possible, pour un p choisit)
g = generator(p)[7]
print("g:",g)
#generateur à donner au serveur

# nombre secret de A
a = 33

# nombre secret de B
b = 67

# A fourni à B => g^a mod p
#Envoyé au serveur
AenvoiaB = (g ** a) % p
print("g^a mod p",AenvoiaB)
print(AenvoiaB)
# B fourni à A => g^b mod p
#Serveur nous envoie
BenvoiaA = (g ** b) % p

# B calcul (g^b mod p) ^ a = g^(b*a) mod p
cleCryptageB = ((AenvoiaB)**b) % p

# A calcul (g^a mod p) ^ b` = g^(b*a) mod p
cleCryptageA = ((BenvoiaA)**a) % p
print(cleCryptageA)

# #On a bien :
# print(cleCryptageB == cleCryptageA)
#
# #notre secret partagé
# serveur = 202
# print((serveur**a)%p)

# #Recap :
# print("--------------------------------------------------------")
# print("n:",p,"g :",g)
# print("g^a mod p",AenvoiaB)

# #notre secret partagé
# serveur = int(input("Entrez une valeur du serveur : "))
# print("Vous avez saisie :",serveur)
# print("Clé à fournir au serveur ",(serveur**a)%p)


# #Saisir la valeur du serveur dans la variable "serveur"
# print("Secret commun :",(serveur**a)%p)


