#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    to25.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: arajapak <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/11/28 11:53:41 by arajapak          #+#    #+#              #
#    Updated: 2024/11/29 10:49:48 by arajapak         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#uer input store numerique variable
#loop while all number form enterd number up to 25
#input number > 25 dispay error and followed by new line

number1 = int(input("Enter a number less than 25: \n"))
if number1 > 25:
    print("Error")
else:
    while number1 <=25:
        print("Inside the loop, my variable is ",number1)
        number1 += 1

