#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    parameter_matching.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: arajapak <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/06 10:50:03 by arajapak          #+#    #+#              #
#    Updated: 2024/12/06 10:50:15 by arajapak         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
#!/bin/python3
import sys

if len(sys.argv) != 2:
    print("none")

else:
    parametre = sys.argv[1]
    user_input = input("whar was the parametre?")
    
    if user_input == parametre:

        print("Good job")
    else:
        print("Nope, sorry...")