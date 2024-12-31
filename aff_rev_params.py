#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    aff_rev_params.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: arajapak <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/04 14:50:11 by arajapak          #+#    #+#              #
#    Updated: 2024/12/04 14:50:19 by arajapak         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
import sys
if len(sys.argv) <= 2:
    print("none")
else:
    for parame in reversed(sys.argv[1:]):
        print(parame)

