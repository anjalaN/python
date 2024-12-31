#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    downcase_all.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: arajapak <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/06 16:49:44 by arajapak          #+#    #+#              #
#    Updated: 2024/12/06 16:49:48 by arajapak         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
#!/bin/python3
import sys
#verification si argumet sont passer ou pas
if len(sys.argv) < 2:
    print("none")
else:
     def downcase_it(chain): #with def creer funtion for string to lower case
          return chain.lower()
     
     for text in sys.argv[1:]:
          print(downcase_it(text))

