# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example,
# the 5-digit number, 15234, is 1 through 5 pandigital.
#
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and
# product is 1 through 9 pandigital.
#
# Find the sum of all products whose multiplicand/multiplier/product identity
# can be written as a 1 through 9 pandigital.
#
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

import itertools
from time import time
start = time()

produits = []

# generation de toutes les permutations
permutation = list(itertools.permutations("123456789"))

# transformation en liste de nombres de 9 chiffres
listePandigital =[]
for nombre in permutation :
    listePandigital.append(''.join(nombre))


# test des deux types de produit pouvant générer une solution :
# nb 1 chiffre * nb 4 chiffres == nb 4 chiffres
# nb 2 chiffres * nb 3 chiffres == nb 4 chiffres
# des conditions plus restreintes sont possibles mais le code est suffisament rapide ainsi
for facteur in listePandigital :
    if int(facteur[0]) * int(facteur[1:5]) == int(facteur[5:9]) :
        produits.append(int(facteur[5:9]))
    if int(facteur[0:2]) * int(facteur[2:5]) == int(facteur[5:9]) :
        produits.append(int(facteur[5:9]))

# list(set()) pour supprimer les doublons
print(sum(list(set(produits))))

print("Temps : " + str(time() - start))