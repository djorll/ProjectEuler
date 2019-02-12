i=1
somme=0
while i < 1000:
    if i%3 == 0:
        somme = somme + i
    elif i%5 == 0:
        somme = somme + i
    i = i + 1
print(somme)