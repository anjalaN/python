#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    your_namebook.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: arajapak <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/09 16:22:24 by arajapak          #+#    #+#              #
#    Updated: 2024/12/09 16:22:35 by arajapak         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
#!/bun/python3
# Fonction qui crée une liste de noms formatée
def array_of_names(persons):
    return [f"{key.capitalize()}: {value.capitalize()}" for key, value in persons.items()]

# Dictionnaire des personnes
persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

# Appel de la fonction et affichage du résultat
print(array_of_names(persons))

