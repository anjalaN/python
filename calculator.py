#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    calculator.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: arajapak <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/11/29 16:12:48 by arajapak          #+#    #+#              #
#    Updated: 2024/11/29 16:12:48 by arajapak         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

number1 = int(input("Give me the first number: "))
number2 = int(input("Give me the second number: "))
print("Thank You!")
result = number1 + number2
print(number1, "+", number2, "=", result)
result = number1 - number2
print(number1, "-", number2, "=", result)
result = number1 / number2
print(number1, "/", number2, "=", int(result))
result = number1 * number2
print(number1, "*", number2, "=", result)
