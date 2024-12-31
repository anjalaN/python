#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count_it.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: arajapak <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/06 10:50:54 by arajapak          #+#    #+#              #
#    Updated: 2024/12/06 10:50:59 by arajapak         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
#!/bin/python3
import sys

if len(sys.argv) < 2:
    print("None")

else:
    print("parametersa  :", len(sys.argv)-1)
    for word in sys.argv[1:]:
        print(word,": ",len(word))

