#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    downcase_it.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: arajapak <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/04 14:48:13 by arajapak          #+#    #+#              #
#    Updated: 2024/12/04 14:48:19 by arajapak         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if len(sys.argv) > 1:
    resusalt_lowercase =(sys.argv[1]).lower()
    print(resusalt_lowercase)
else:
    print("none")


