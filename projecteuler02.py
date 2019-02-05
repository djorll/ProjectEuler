a,b = 1,1
somme = 0

while a<4000000 :
    a,b = b,a+b
    if a%2 == 0:
        somme = somme + a

print(somme)
