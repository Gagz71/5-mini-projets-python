"""
Programme jeu pierre - papier - ciseaux
"""

# Initialisation des variables dans un tableau
import random

choice = ['Pi', 'P', 'C']
cpu_score = 0
user_score = 0


print('Veuillez saisir votre élément: ')

while True:

    cpu_choice = random.choice(choice)
    user_choice = str(input('Pierre (pi)  ? Papier (p) ? ou Ciseaux (c) ?  "q" pour quitter ')).capitalize()

    # Si l'élément choisi par l'user est le même que celui du cpu
    if user_choice == cpu_choice:
        print('Egalité !')

    # Si l'user choisi la pierre
    elif user_choice == 'Pi':
        # si le cpu a choisi le papier
        if cpu_choice == 'P':
            print('Vous perdez. Le papier du cpu recouvre votre pierre.')
            cpu_score += 1
        # ou si le cpu a choisi les ciseaux
        elif cpu_choice == 'C':
            print('Vous gagnez ! Votre pierre casse les ciseaux du cpu !')
            user_score += 1

    # Si l'user choisit le papier
    elif user_choice == 'P':
        # si le cpu a choisi la pierre
        if cpu_choice == 'Pi':
            print('Vous gagnez ! Votre papier recouvre la pierre du cpu ! ')
            user_score += 1
        # ou si le cpu a choisi les ciseaux
        elif cpu_choice == 'C':
            print('Vous perdez. Les ciseaux du cpu découpent votre papier !')
            cpu_score += 1

    # Si l'user choisit les ciseaux
    elif user_choice == 'C':
        # si le cpu a choisi la pierre
        if cpu_choice == 'Pi':
            print('Vous perdez. La pierre du cpu cassent vos ciseaux ! ')
            cpu_score += 1
            # si le cpu a choisi le papier
        elif cpu_choice == 'P':
            print('Vous gagnez ! Vos ciseaux découpent le papier du cpu !')
            user_score += 1

    # Si l'user choisit de quitter
    elif user_choice == 'Q':
        print("Résultats : ")
        if user_score > cpu_score:
            print(f"Bravo !!! \n Vous avez remporté cette manche avec un score de {user_score} points contre {cpu_score} points pour le cpu ! ")
        elif user_score < cpu_score:
            print(f"LOOSER ! \nVous avez perdu cette manche avec un score de {user_score} points contre {cpu_score} points pour le cpu. \n Retentez votre chance !")
        elif user_score == cpu_score:
            print(f"Egalité ! Vous et le cpu avez fait un score de {user_score} points ! \n Départagez-vous en retentant votre chance !")
        break
    else:
        print('Elément choisi incorrecte. Veuillez saisir p pour le papier, pi pour la pierre ou c pour les ciseaux.')