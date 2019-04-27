# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a
# perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if
# this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as
# the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater
# than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced
# any further by analysis even though it is known that the greatest number that cannot be expressed as
# the sum of two abundant numbers is less than this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
from time import time

start = time()

def diviseurs(nb, extremum=False):
    diviseurs = []
    inf = 1 if extremum else 2
    for i in range(inf, int(nb ** 0.5) + 1):
        q, r = divmod(nb, i)
        if r == 0:
            if q >= i:
                diviseurs.append(i)
                if q > i:
                    diviseurs.append(nb // i)
    return diviseurs


def est_abondant(n):
    return sum(diviseurs(n)) + 1 > n


# Génération d'une liste contenant tous les nombres abondants
# inférieurs à 28124
abondants = [i for i in range(2, 28124) if est_abondant(i)]

# calcul da la somme de tous les nombres créés par la somme de 2 abondants et inférieures à 28123
# les sommes sont écrites dans un dictionnaire pour éviter les doublons
sommes = {}
for i in range(len(abondants)):
    for j in range(i, len(abondants)):
        somme = abondants[i] + abondants[j]
        if somme > 28123:
            break
        sommes[somme] = 1

# Différence entre la somme de tous les nombres jusqu'à 28123 et la somme générée précédement

resultat = (28123 * 28124) // 2 - sum(sommes.keys())

print(resultat)
print("Temps : " + str(time() - start))

