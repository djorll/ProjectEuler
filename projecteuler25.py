a,b = 1,1
somme = 0
resultat = 2

while len(str(b)) < 1000 :
    a, b = b, a+b
    resultat += 1
print(resultat)
