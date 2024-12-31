#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    append_it.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: arajapak <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/06 10:52:30 by arajapak          #+#    #+#              #
#    Updated: 2024/12/06 10:52:34 by arajapak         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/bin/python3
import sys

import sys
if len(sys.argv) < 2:
    print("none")
else:
    for word in sys.argv[1:]:
        if word.endswith('ism'):
            continue
        else:
            print(word+'ism')