# liste les diviseurs de n hors n
def getFactors(n):
    factors=[];
    for i in range(1, int((n / 2)+1)):
        if n % i == 0:
            factors.append(i)
    return factors

resultat = 0
for i in range(1, 10000):
    j = sum(getFactors(i))
    if sum(getFactors(j)) == i and i != j:
        resultat += i
print(resultat)