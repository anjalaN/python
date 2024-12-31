#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    upcase_it.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: arajapak <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/04 14:47:41 by arajapak          #+#    #+#              #
#    Updated: 2024/12/04 14:47:49 by arajapak         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if len(sys.argv) > 1:
    resusalt_uppercase =(sys.argv[1]).upper()
    print(resusalt_uppercase)
else:
    print("none")
    
