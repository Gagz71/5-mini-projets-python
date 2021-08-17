"""Mini-lancé de dé
# L'user va taper une touche y
# ce qui aura pr conséquence de générer un chiffre aléatoire entre 1 et 6
"""
import random

# boucle while pour afficher le jeu tant que l'user veut jouer (devra saisir chiffre 0 pour quitter)
while True:

    # demande à l'user de saisir un chiffre entier entre 1 et 6
    # int(input()) = pour que l'user ne puisse saisir qu'un entier
    x = int(input("veuillez saisir un chiffre entre 1 et 6: "))

    # Si l'user saisit 0
    if x == 0:
        # affichage d'un message d'aurevoir
        # arrêt du programme
        print('Fermeture du lancé de dé')
        break

    elif x == 1 or x == 2 or x == 3 or x == 4 or x == 5 or x == 6:
        # Affichage d'un nombre entier aléatoire entre 1 et 6
        result = print(random.randint(1,6))

        if x == result:
            print('Bien joué vous avez trouvé le bon chiffre')
            test2 = input('voulez-vous rejouer ? (o/n)' )

            if test2 == 'n':
                break


        else:
            print('Vous n`\avez pas trouvé le bon chiffre. Retentez votre chance !')
            break

    else:
        print('Commande incorrecte. Veuillez saisir un chiffre entre 1 et 6 pour continuer, ou 0 pour fermer')
