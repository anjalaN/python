#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    play_with_arrays.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: arajapak <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/02 12:44:51 by arajapak          #+#    #+#              #
#    Updated: 2024/12/02 12:44:56 by arajapak         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
import array 
number_array =[2, 8, 9, 48, 8, 22, -12, 2]
print(number_array)

new_array = [2 + new_list for new_list in number_array if new_list> 5]
print(new_array)
