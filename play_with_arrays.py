#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    play_with_arrays.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: arajapak <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/02 12:45:27 by arajapak          #+#    #+#              #
#    Updated: 2024/12/02 12:45:31 by arajapak         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
import array 
number_array = [2, 8, 9, 48, 8, 22, -12, 2]
print(number_array)
new_array = {2 + list for list in number_array if list > 5}
print(new_array)

