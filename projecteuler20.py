def fact(n):
    x=1
    for i in range(2,n+1):
        x*=i
    return x

chiffres = [int(c) for c in str(fact(100))]

print(sum(chiffres))

# variable chiffre par clarte mais pas indispensable
# print(sum(int(c) for c in str(fact(100)))) suffit