def eratosthene(n):
    """retourne la liste des nombres premiers <= n (crible d'eratosthene)"""
    if n<2:
        return []
    n += 1
    # on créé un tableau de longueur n avec un TRUE (possiblement premier) ou FALSE (non premier)
    tableau = [False,False] + [True]*(n-2)
    tableau[2::2] = [False]*((n-2)//2 + n%2) # sup. des nb pairs
    premiers = [2] # initialisation de la tableau des nb 1ers (2 est 1er)
    # quand on cherche les diviseurs de n, il est inutile d'aller au delà de la racine de n
    racine = int(n**0.5) # pas la peine de dégainer un math.sqrt quand **0.5 suffit
    racine = racine + [1,0][racine%2] # pour que racine soit impair, le modulo détermine quel élément de la liste [1,0] on ajoute
    for i in range(3, racine+1, 2):
        if tableau[i]:
            # on enregistre le nouveau nb 1er
            premiers.append(i)
            # on élimine i et ses multiples
            tableau[i::i] = [False]*((n-i)//i + int((n-i)%i>0)) 
    for i in range(racine, n, 2): # pour i des valeur sqrt(n) à n avec un pas de 2
        if tableau[i]:
            # on enregistre le nouveau nb 1er (pas de multiples à supprimer)
            premiers.append(i)
    return premiers

print(sum(eratosthene(2000000)))
