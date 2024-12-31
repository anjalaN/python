# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    mult.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: arajapak <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/11/26 14:27:08 by arajapak          #+#    #+#              #
#    Updated: 2024/11/26 14:39:47 by arajapak         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/bin/python3
#prompt user to enter two number
#multification with number positive ,negative and zero
#display multification

number1 = int(input("Enter the first number:"))
number2 = int(input("Enter the second number:"))
result = number1 * number2

if result > 0:
    print(number1, "x", number2, "=", result)
    print("The result is positive.")
elif result < 0:
    print(number1, "x", number2, "=", result)
    print("The result is negative.")
else:
    print(number1, "x", number2, "=", result)
    print("The result is positive and ngative.")



