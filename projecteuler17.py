# liste des mots sans faute d'ortograf
unites = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
dizaines = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
autre = ['hundred', 'thousand', 'and']
longueurtexte = 0
#Calcul du nombre de lettres a utiliser pour ecrire les nombres de 1 a 1000
for i in range(1, 1001):
    #Stockage des valeurs par puissance de 10 selon la methode de l'exercice 16
    unite = i%10
    dizaine = (i//10)%10
    centaine = (i//100)%10
    millier = (i//1000)%10
    # si le rang milier different de 0 ajout de "one" et "thousand"
    if millier != 0:
        longueurtexte += len(unites[0]) + len(autre[1])
    else:
        # si le rang centaine different de 0
        if centaine != 0:
            # ajout du nombre de centaine + "hundred"
            longueurtexte += len(unites[centaine-1]) + len(autre[0])
            # si on est pas sur une centaine juste, ajouter "and"
            if i%100 != 0:
                longueurtexte += len(autre[2])
        # calcul de dizaines et unites
        if i%100 != 0:
            # quand on est en dessus de 20 on regarde la liste unite et on a fini pour cette valeur de i
            if dizaine < 2:
                longueurtexte += len(unites[i%100-1])
            # a partir de 20 il faut additionner dizaine et unite
            else:
                longueurtexte += len(dizaines[dizaine-2])
                if unite != 0:
                    longueurtexte += len(unites[unite-1])

print(longueurtexte)