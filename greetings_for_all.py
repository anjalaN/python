#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    greetings_for_all.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: arajapak <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/06 16:50:44 by arajapak          #+#    #+#              #
#    Updated: 2024/12/06 16:50:54 by arajapak         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
#!/bin/python3

import sys

def greeting(name=None):
    if name is None or not isinstance(name, str):
        print("Error! It was not a name")
    else:
        print(f"Hello, {name}.")

# Appel correct de la fonction
greeting('Alexandra')
greeting('Wil')
greeting(' ' )
greeting(42)

