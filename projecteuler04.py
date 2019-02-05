i = 100
solution = 0
resultat = 0
while i < 1000:
    j = 100
    while j < 1000:
        resultat = i * j
        if str(resultat) == "".join(reversed(str(resultat))):
            if i * j > solution:
                solution = i * j
        j = j + 1
    i = i + 1

print(solution)
