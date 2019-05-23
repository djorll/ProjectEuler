# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
# 
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# 
# How many circular primes are there below one million?

from time import time
start = time()
# fonction pour générer la liste des premiers
# version commentée de la fonction dans projecteuler10 Summation of primes.py

def eratosthene(n):
    if n < 2:
        return []
    n += 1
    tableau = [False, False] + [True] * (n - 2)
    tableau[2::2] = [False] * ((n - 2) // 2 + n % 2)
    premiers = [2]
    racine = int(n ** 0.5)
    racine = racine + [1, 0][racine % 2]
    for i in range(3, racine + 1, 2):
        if tableau[i]:
            premiers.append(i)
            tableau[i::i] = [False] * ((n - i) // i + int((n - i) % i > 0))
    for i in range(racine, n, 2):
        if tableau[i]:
            premiers.append(i)
    return premiers

# fonction pour tester les chiffres générés
def est_premier(nb):
    if nb == 1:
        return False
    if nb%2 == 0:
        return False
    for i in range(3, int(nb**0.5)+1, 2):
        if nb%i == 0:
            return False
    return True

# fonction pour effectuer les permutations circulaires
def circulaire(s):
    circulaire = [s]
    i = 0
    while i < len(s)-1:
        s = s[(len(s)-1):len(s)] + s[0:(len(s)-1)]
        circulaire.append(s)
        i += 1
    return (circulaire)

listepremiers = eratosthene(1000000)

circularprime = 0

for nb in listepremiers:
     listecirculaire = circulaire(str(nb))
     for chiffre in listecirculaire:
        test = 0
        if est_premier(int(chiffre)) == True:
            test += 1
     if test == len(listecirculaire):
        circularprime += 1

print(circularprime)

print("Temps : " + str(time() - start))

