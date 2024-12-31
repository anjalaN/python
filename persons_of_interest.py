# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    persons_of_interest.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: arajapak <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/13 10:31:10 by arajapak          #+#    #+#              #
#    Updated: 2024/12/13 10:31:29 by arajapak         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3
#donne des information
women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecilia Payne", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

# Fonction pour afficher les scientifiques triés par date de naissance
def famous_births():
    # Trier les scientifiques par date de naissance (convertir en entier pour trier correctement)
    sorted_scientists = sorted(women_scientists.values(), key=lambda x: int(x['date_of_birth']))
    
    # Affichage des scientifiques triés
    for scientist in sorted_scientists:
        print(f"{scientist['name']} is a great scientist born in {scientist['date_of_birth']}")

# Appel de la fonction
famous_births()