# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
# 
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
# 
# (Please note that the palindromic number, in either base, may not include leading zeros.)

from time import time
start = time()

# les deux fonctions revoient True ou False
def estPal(number):
    number = str(number)
    return (number == number[::-1])
def estPalBin(number):
    number = f"{number:b}" #ne fonctionne qu'avec Python 3, a ameliorer
    return (number == number[::-1])

# le sum permet l'économie d'une boucle avec variable
print(sum(x for x in range(1000000) if estPal(x) and estPalBin(x)))
print("Temps : " + str(time() - start))
