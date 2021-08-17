"""
Programme qui demande à l'user de deviner le nombre qu'il aura tiré aléatoirement
"""
import random

nb_to_find = random.randint(1,9)
user_score = 0

# Boucle for pour ne laisser que 3 essais à l'user
for i in range(3):
    user_nb = int(input('Veuillez saisir un chiffre entre 1 et 9: '))

    if user_nb == nb_to_find:
        user_score = 1
        break
    elif user_nb > nb_to_find:
        print(f'Le chiffre à trouver est inférieur à {user_nb}')
    elif user_nb < nb_to_find:
        print(f'Le chiffre à trouver est supérieur à {user_nb}')
    else:
        print('Saisi incorrecte. Veuille saisir un chiffre entre 1 et 9: ')


if user_score == 1:
    print('Bravo ! Vous avez trouvé le bon chiffre !')
    print(f'Le nb à trouver était bien: {user_nb} ')
else:
    print(f'Vous avez perdu. Le nb à trouver était : {nb_to_find} ')

