# Euler discovered the remarkable quadratic formula:
#
# n2+n+41
#
# It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39
#   . However, when n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41
#   is clearly divisible by 41.
#
# The incredible formula n2−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤79.
# The product of the coefficients, −79 and 1601, is −126479.
#
# Considering quadratics of the form:
#
#     n2+an+b, where |a|<1000 and |b|≤1000 where |n| is the modulus/absolute value of n e.g. |11|=11 and |−4|=4
#
# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum
# number of primes for consecutive values of n, starting with n=0.

# b est forcément premier car c'est la valeur pour n = 0
# a est forcement impair car pour n = 1 a+b+1 est premier

# définition de la liste des premiers < 1000

from time import time
start = time()


def eratosthene(p):
    if p < 2:
        return []
    p += 1
    tableau = [False, False] + [True] * (p - 2)
    tableau[2::2] = [False] * ((p - 2) // 2 + p % 2)
    premiers = [2]
    racine = int(p ** 0.5)
    racine = racine + [1, 0][racine % 2]
    for i in range(3, racine + 1, 2):
        if tableau[i]:
            premiers.append(i)
            tableau[i::i] = [False] * ((p - i) // i + int((p - i) % i > 0))
    for i in range(racine, p, 2):
        if tableau[i]:
            premiers.append(i)
    return premiers


def isprime(m):
    # Corner cases
    if m <= 1:
        return False
    if m <= 3:
        return True

    # This is checked so that we can skip
    # middle five numbers in below loop
    if m % 2 == 0 or m % 3 == 0:
        return False

    i = 5
    while i * i <= m:
        if m % i == 0 or m % (i + 2) == 0:
            return False
        i = i + 6

    return True

# liste des nombres premiers inférieurs à 1000
# premiers = eratosthene(1000)


longueurMax = 0
resultat = 0
resultat_a = 0
resultat_b = 0
# b prend successivement la valeur des différents nombres premiers
for b in eratosthene(1000):
    # a prend successivement la valeur de tous les nombres impairs de -999 à 1000
    for a in range(-999, 1000, 2):
        coef = b
        n = 0
        # Calcul du nombre consécutif de nombres premiers
        while isprime(coef):
            n += 1
            coef = n**2 + a*n + b
        if n > longueurMax:
            longueurMax = n
            resultat = a*b
            resultat_a = a
            resultat_b = b

print(resultat, resultat_a, resultat_b, longueurMax)
print("Temps : " + str(time() - start))
