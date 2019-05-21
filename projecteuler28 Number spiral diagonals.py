# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
#
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
#
# It can be verified that the sum of the numbers on the diagonals is 101.
#
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

# carré taille 3x3, on prend les chiffres de 2 en 2, taille 4x4 de 4 en 4...

from time import time
start = time()

tailleCarre = 3
somme = 1
position = 1
facteur = 2

while tailleCarre < 1002:
    i = 1
    while i < 5:
        position += facteur
        somme += position
        i += 1
    facteur += 2
    tailleCarre += 2  # j'avais oublié que la taille du carré évolue de 2 en 2

print(somme)
print("Temps : " + str(time() - start))
