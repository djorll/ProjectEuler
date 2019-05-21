# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# 
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# 
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

# détermination valeur max
# max pour nb de 6 chiffre = 6 x 9! = 2 177 280 possible
# max pour nb de 7 chiffre = 6 x 9! = 2 540 160 possible
# max pour nb de 6 chiffre = 6 x 9! = 2 903 040 possible


from time import time
start = time()

i = 3
somme_resultat = 0

# l'utilisation d'un dictionnaire pour les factorielle de 0 à 9 est plus rapide 
# que le calcul via math.factorial
fact_chiffres = {
0:1,
1:1,
2:2,
3:6,
4:24,
5:120,
6:720,
7:5040,
8:40320,
9:362880,
}

for i in range (3,1000000) :
    chiffre = []
    for j in str(i):
        chiffre.append(j)
    # je ne teste que les cas ou le nombre est bien supérieur à la factorielle de son plus grand chiffre
    if i > fact_chiffres[int(max(chiffre))]: 
        somme_fact = 0
        for nb in chiffre :
            somme_fact += fact_chiffres[int(nb)]
        if somme_fact == i :
            somme_resultat += somme_fact

print(somme_resultat)

print("Temps : " + str(time() - start))
