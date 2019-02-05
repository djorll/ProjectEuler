import math


def nombrePremierJusqua(x):
    premier = [2]
    i = 3

    while i < x:
        verif = 1
        for p in premier:
            if (i % p) == 0:
                verif = 0
                break

        if verif == 1:
            premier.append(i)

        i = i + 1

    return premier


print(nombrePremierJusqua(120000)[10000])
