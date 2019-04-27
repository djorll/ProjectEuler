# n! means n × (n − 1) × ... × 3 × 2 × 1
#
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!


def fact(n):
    x=1
    for i in range(2,n+1):
        x*=i
    return x

chiffres = [int(c) for c in str(fact(100))]

print(sum(chiffres))

# variable chiffre par clarte mais pas indispensable
# print(sum(int(c) for c in str(fact(100)))) suffit