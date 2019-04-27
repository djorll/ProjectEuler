# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

from time import time
start = time()

def est_premier(nb):
    if nb == 1:
        return False
    if nb%2 == 0:
        return False
    for i in range(3, int(nb**0.5)+1, 2):
        if nb%i == 0:
            return False
    return True

rang_nbpremier = 1
i = 1
while rang_nbpremier != 10001:
    i += 2
    if est_premier(i):
        rang_nbpremier += 1
print(i)

print("Temps : " + str(time() - start))
