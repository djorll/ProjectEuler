# The nombre 3797 has an interesting property. Being premier itself, it is possible to continuously 
# remove digits from left to right, and remain premier at each stage: 3797, 797, 97, and 7. Similarly 
# we can work from right to left: 3797, 379, 37, and 3.
# 
# Find the sum of the only eleven premiers that are both truncatable from left to right and right to left.
# 
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable premiers.

from time import time
start = time()

# on va générer une liste de nombre premiers à l'aide du du crible d'Eratosthene
# créé dans le problème 10

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

# on fait l'hypothèse que les premiers possibles sont inférieurs à 1 000 000
# on pourra augmenter cette valeur si la solution est incomplète

premiers = eratosthene(1000000)
solutions = list(premiers)

# on retire 2,3,5,7 comme précisé dans l'énoncé

solutions.remove(2)
solutions.remove(3)
solutions.remove(5)
solutions.remove(7)

# élimination de tous les premiers comportant un pair ou un 5
# ailleurs qu'en première position et qui échoueront au test 
# de tronquabilité

sanspair = list(solutions)
for nombre in sanspair:
    produit = 1
    chiffres = [int(c) for c in str(nombre)]
    del chiffres[0]
    for chiffre in chiffres:
        produit *= chiffre
    if produit%2 == 0 or produit%5 == 0:
            solutions.remove(nombre)

# test de la tronquabilité à droite

droite = list(solutions)
for nombre in droite:
    test = str(nombre)
    i = len(test)
    while i > 1:
        test = test[:-1]
        i -= 1
        if int(test) not in premiers:
            solutions.remove(nombre)
            break

# test de la tronquabilité à gauche

gauche = list(solutions)
for nombre in gauche:
    test = str(nombre)
    i = len(test)
    while i > 1:
        test = test[1:]
        i -= 1
        if int(test) not in premiers:
            solutions.remove(nombre)
            break

print(sum(solutions))

print("Temps : " + str(time() - start))