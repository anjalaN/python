#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    free_range.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: arajapak <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/06 10:53:14 by arajapak          #+#    #+#              #
#    Updated: 2024/12/06 10:53:19 by arajapak         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/bin/python3
import sys
if len(sys.argv) == 3:
    start = int(sys.argv[1])
    end = int(sys.argv[2]) + 1
    print(list(range(start, end)))
else:
    print("none")



