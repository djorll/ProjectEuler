# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2^1000?


from time import time

start = time()
somme = 0
bignumber = 2 ** 1000

while bignumber > 0:
    somme += bignumber % 10
    bignumber = bignumber // 10

print(somme)
print("Temps : " + str(time() - start))
