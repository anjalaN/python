#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    scan_it.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: arajapak <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/04 14:50:46 by arajapak          #+#    #+#              #
#    Updated: 2024/12/04 14:50:52 by arajapak         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
#!/bin/python3
import sys
import re

if len(sys.argv) == 3:
    
    first  = sys.argv[1]
    second = sys.argv[2]
    serche = re.findall(first, second)
    if(len(serche)) == 0:
        print("none")
    else:
        print(len(serche))
else:
    print("none")




    