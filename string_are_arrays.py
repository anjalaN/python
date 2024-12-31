#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    string_are_arrays.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: arajapak <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/06 10:51:56 by arajapak          #+#    #+#              #
#    Updated: 2024/12/06 10:52:01 by arajapak         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
#!/bin/python3
import sys

if len(sys.argv) < 2:
    print("None")
else:
    text = sys.argv[1]
    result = '' .join([char for char in text if char == 'z'])

    if result:
        print(result)
    else:
        print("none")
