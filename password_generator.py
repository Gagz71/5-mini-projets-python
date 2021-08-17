""" Programme qui va générer un mot de passe aléatoire dont la longueur sera choisi par l'user
"""
import random

# demande à l'user de saisir la longueur voulu du mot de passe
# int pour que l'user ne puisse seulement rentrer qu'un nombre entier
passlength = int(input("veuillez saisir la longueur de votre nouveau mot de passe généré: "))

caractères = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.!?:#;,ù%$'

# random.sample(caractères a choisir, nb d'occurence à choisir)
# -> va créer un tableau de caractères

# méthod join permet de coller les éléments d'un tableau, guillemet permettent de dire par quoi les éléménts sont séparés => ici par rien on veut juste que les caractères soient tous collés
generated_pass = "".join(random.sample(caractères, passlength))

# affichage nouveau mot de passe généré
print('Votre nouveau mot de passe est: ' + generated_pass)
