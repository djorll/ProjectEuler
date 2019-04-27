# You are given the following information, but you may prefer to do some research for yourself.
#
#     1 Jan 1900 was a Monday.
#     Thirty days has September,
#     April, June and November.
#     All the rest have thirty-one,
#     Saving February alone,
#     Which has twenty-eight, rain or shine.
#     And on leap years, twenty-nine.
#     A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?


# oui  avec import datetime ça serait facile
# mais vu l'enonce je suppose qu'on est pas sense l'utiliser
# on va gerer la date comme une liste date = [jour, mois, annee]
# on part du 1er dimanche 1901 (merci excel)

date = [6, 1, 1901]


# une fonction pour avoir la date du dimanche suivant
def get_dimanche_suivant(date):
    # nombre de jours par mois
    month_len = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # Test bissextile
    if date[2] % 4 == 0 and (date[2] % 100 != 0 or date[2] % 400 == 0):
        month_len[1] = 29
    # On augmente le nombre de jour de 7
    date[0] += 7
    # si le nouveau nombre de jour est superieur à la taille du mois
    # on incremente le mois et on garde le restant du nombre de jours
    if date[0] > month_len[date[1]-1]:
        date[0] = date[0] - month_len[date[1]-1]
        date[1] += 1
    # si mois > 12 on ajoute un an et on met le mois à 1,
    if date[1] > 12:
        date[1] = 1
        date[2] += 1
    return date


resultat = 0

# on teste tous les dimanches et on stoppe dès qu'on arrive à 2001

while date[2] != 2001:
    if date[0] == 1:
        resultat += 1
    date = get_dimanche_suivant(date)
print(resultat)
