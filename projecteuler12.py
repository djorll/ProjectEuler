from time import time

start = time()


# fonction qui donne la liste des diviseurs de n (1 et n compris)

def diviseurs(n):
    diviseurs = []
    for i in range(1, int(n ** 0.5) + 1):
        quotient, reste = divmod(n, i)
        if reste == 0:
            if quotient >= i:
                diviseurs.append(i)
                if quotient > i:
                    diviseurs.append(n // i)
    return diviseurs


pyramide = 3
rang = 2
nombre_diviseurs = 0
while nombre_diviseurs < 500:
    # calcul de la nouvelle pyramide
    rang += 1
    pyramide += rang
    # calcul du nombre de diviseurs
    nombre_diviseurs = len(diviseurs(pyramide))

print(pyramide)
print("Temps : " + str(time() - start))
