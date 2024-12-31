#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    play_with_arrays.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: arajapak <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/02 12:44:06 by arajapak          #+#    #+#              #
#    Updated: 2024/12/02 12:44:10 by arajapak         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import array 
number_array =[2, 8, 9, 48, 8, 22, -12, 2]
new_array = [2 + item for item in number_array]

print("Original array: ", number_array)
print("New array: ",new_array)

