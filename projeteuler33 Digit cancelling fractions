# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8,
# which is correct, is obtained by cancelling the 9s.
# 
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
# 
# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
# 
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.


# non trivial => pas de zéro dans le numérateur et le dénominateur
# pour chaque numérateur de 11 à 99, tester les numérateurs ayant au moins un chiffre en commun
# puis comparer le rapport numérateur / dénominateur avec et sans ce chiffre commun  

# pour trouver les 4 fractions qui fonctionnent

# resultat = {}
# numerateur = 1
# denominateur = 1
# 
# for i in range (1,10) :
#     for j in range (1,10) :
#         if i / j < 1 and i != j :
#             for x in range (1,10) :
#                 if x != i and x != j :
#                     num1 = "{}{}".format(i,x)
#                     num2 = "{}{}".format(x,i)
#                     den1 = "{}{}".format(j,x)
#                     den2 = "{}{}".format(x,j)
#                     if int(num1) / int(den1) == i / j :
#                         resultat[num1] = den1
#                     if int(num1) / int(den2) == i / j :
#                         resultat[num1] = den2
#                     if int(num2) / int(den1) == i / j :
#                         resultat[num2] = den1
#                     if int(num2) / int(den2) == i / j :
#                         resultat[num2] = den2
# 
# print(resultat)


from time import time
start = time()

def gcd(a, b):
    '''gcd retourne le plus grand commun diviseur (greatest common divisor) 
       de 2 entiers donnés.'''
    while b:
        a, b = b, a%b
    return a

def simplifier(a, b):
    '''divise deux entiers par leur facteur commun.'''
    facteur_commun = gcd(a, b)
    a /= facteur_commun
    b /= facteur_commun
#    return a, b je ne veux que le denominateur
    return b

resultat = {}
numerateur = 1
denominateur = 1

for i in range (1,10) :
    for j in range (1,10) :
        if i / j < 1 and i != j :
            for x in range (1,10) :
                if x != i and x != j :
                    num1 = "{}{}".format(i,x)
                    num2 = "{}{}".format(x,i)
                    den1 = "{}{}".format(j,x)
                    den2 = "{}{}".format(x,j)
                    if int(num1) / int(den1) == i / j or int(num1) / int(den2) == i / j or int(num2) / int(den1) == i / j or int(num2) / int(den2) == i / j :
                        numerateur *= i
                        denominateur *= j

print(simplifier (numerateur,denominateur))

print("Temps : " + str(time() - start))
