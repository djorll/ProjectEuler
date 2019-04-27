# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#
#It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been
# proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.


from time import time

start = time()
# initialisation du dictionnaire
dico_collatz = {1: 0}


# calcul recursif de la suite
def suite_collatz(nb):
    # Si nb existe dans le dictionnaire, on retourne 
    # la longueur enregistree pour cette valeur
    if nb in dico_collatz:
        return dico_collatz[nb]
    # Si nb n'est pas dans le dico, on calcule le terme suivant
    # et par recursivite de terme en terme 
    # tant qu'il n'est pas dans le dico
    # l'execution pas a pas montre que ces valeurs sont 
    # stockee en memoire
    if nb % 2 == 0:
        longueur = suite_collatz(nb // 2)
    else:
        longueur = suite_collatz(3 * nb + 1)
    # un fois un terme trouve dans le dico, 
    # on rebalaye les valeurs stockee recursivement
    # leur longueur = longueur valeur precedente + 1
    # puis on stocke le couple valeur longueur dans le dico
    longueur += 1
    dico_collatz[nb] = longueur
    return longueur


# variable pour stocker temporairement la longueur
# et l'ajouter a resultat si c'est la plus longue
resultat = 0
maximum = 0
for i in range(1, 1000000):
    longueur = suite_collatz(i)
    if longueur > maximum:
        resultat = i
        maximum = longueur

print(resultat)
print("Temps : " + str(time() - start))
