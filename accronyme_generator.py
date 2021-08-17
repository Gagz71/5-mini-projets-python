"""
Programme qui va demander à l'user de saisir une string et transformer cette string en accronyme :
va prendre seulement les initiales des mots pour en faire un seul mot
-> va diviser string en plusieurs éléments
"""

# Demande à l'user un string
userText = str(input('Veuillez saisir une chaine de caractères: '))

# création de la fonction
def accro_generator(string):
    # méthode split permet de diviser string en caractèresn car string est récupéré dans tableau -> conversion tableau de caractères en une string
    words = string.split()
    # initialisation de la variable à vide
    accro = ''

    # boucle qui va parcourir les lettres des mots
    for i in words:
        # première lettre vaut 0 et nous on veut que la première lettre
        # upper pour que ce soit en maj
        accro = accro + str(i[0]).upper()
    #ne pas oublier le return pour l'output
    return accro;


result = accro_generator(userText)

print('mot saisi: '+ userText)
# autre façon d'afficher une variable => f" {variable}"
print(f"accronyme du mot saisi: {result}")
