def diviseurs(nb, extremum = False):
    diviseurs = []
    inf = 1 if extremum else 2
    for i in range(inf, int(nb**0.5)+1):
        q, r = divmod(nb, i)
        if r == 0:
            if q >= i:
                diviseurs.append(i)
                if q > i:
                    diviseurs.append(nb//i)
    return diviseurs

def est_abondant(n):
    return sum(diviseurs(n))+1 > n


#Génération d'une liste contenant tous les nombres abondants
#inférieurs à 28124
abondants = [i for i in range(2, 28124) if est_abondant(i)]

print(abondants)
