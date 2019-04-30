# In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
#
#     1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
#
# It is possible to make £2 in the following way:
#
#     1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
#
# How many different ways can £2 be made using any number of coins?

from time import time
start = time()

resultat = 0
reste = 200
for l2 in range(0, reste+1, 200):
    reste = 200 - l2
    for l1 in range(0, reste+1, 100):
        reste = 200 - l2 - l1
        for p50 in range(0, reste+1, 50):
            reste = 200 - l2 - l1 - p50
            for p20 in range(0, reste+1, 20):
                reste = 200 - l2 - l1 - p50 - p20
                for p10 in range(0, reste+1, 10):
                    reste = 200 - l2 - l1 - p50 - p20 - p10
                    for p5 in range(0, reste+1, 5):
                        reste = 200 - l2 - l1 - p50 - p20 - p10 - p5
                        for p2 in range(0, reste+1, 2): # le resultat est forcement complété par des pièces de 1
                            resultat += 1

print(resultat)
print("Temps : " + str(time() - start))

# google a trouvé mieux :
# cible = 200
# pieces = [1, 2, 5, 10, 20, 50, 100, 200]
# combinaisons = [1] + [0]*cible
#
# for piece in pieces:
#     for i in range(piece, cible+1):
#         combinaisons[i] += combinaisons[i-piece]
#
# print (combinaisons[cible])
#
# "This code is indeed brilliant, but I have no idea how it works!"