# merci python pour les outils existants
import itertools
permutation = list(itertools.permutations("0123456789"))[999999]
resultat = ''.join(permutation)
print(resultat)
