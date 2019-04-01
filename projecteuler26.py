
def f(numerateur, denominateur):
    x = numerateur * 9
    z = x
    k = 1
    while z % denominateur:
        z = z * 10 + x
        k += 1
    return k, z / denominateur
    
denominateur = 2
resultat = []

while denominateur < 1001:
    if 1/(1/float(denominateur)) != denominateur:
        resultat.append(f(denominateur))
        denominateur += 1

print(resultat.sort(reverse=True)[0])
