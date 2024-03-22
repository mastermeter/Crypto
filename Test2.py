def puissances_fractionnees(base, exposant):
    result = 1
    puissance_deux = base

    # Convertir l'exposant en binaire
    exposant_binaire = bin(exposant)[2:]  # Ignorer le préfixe '0b'

    # Parcourir chaque bit de l'exposant
    for bit in exposant_binaire[::-1]:  # Inverser la chaîne binaire pour commencer par les bits de poids faible
        if bit == '1':
            result *= puissance_deux
        puissance_deux *= puissance_deux  # Calculer la puissance de la puissance de 2 suivante

    return result

base = 34
exposant = 677
resultat = puissances_fractionnees(base, exposant)
print(resultat)