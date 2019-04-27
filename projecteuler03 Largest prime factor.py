# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

# oui j'ai piqué la formule sur le ouèbe
def decompose(n):
    print("%d = 1" % n, end=' ')
    i = 2
    while n > 1:
        while n % i == 0:
            print("x", i, end=' ')
            n = n / i
        i = i + 1
    print("\n")  # saut de ligne


print(decompose(600851475143))
