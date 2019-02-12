from time import time

start = time()


def nombrepremierjusqua(x):
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


print(nombrepremierjusqua(120000)[10000])
print("Temps : " + str(time() - start))
