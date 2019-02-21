from time import time

start = time()
somme = 0
bignumber = 2 ** 1000

while bignumber > 0:
    somme += bignumber % 10
    bignumber = bignumber // 10

print(somme)
print("Temps : " + str(time() - start))
