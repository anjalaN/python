#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    advanced_mult.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: arajapak <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/11/28 12:21:35 by arajapak          #+#    #+#              #
#    Updated: 2024/11/28 12:21:45 by arajapak         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/bin/python3
#use two while loop

i = 0
while i < 11:
    row = "Table of "  +str(i)+ " "  ":" " "
    j = 0
    while j < 11:
        row += str(i * j)   + '' " "
        
        j += 1
    
    print(row.strip())
    i +=  1
