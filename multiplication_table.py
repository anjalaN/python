#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    multiplication_table.py                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: arajapak <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/11/28 12:13:08 by arajapak          #+#    #+#              #
#    Updated: 2024/11/28 12:15:23 by arajapak         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#user input numerique variable and print
#conditon with while loop
number1 = int(input("Enter a number:\n"))
i = 0
while i <= 12:
    result = number1 * i
    print(number1, "x", i, "=", result)
    i += 1





