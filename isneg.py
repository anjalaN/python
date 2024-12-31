# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    isneg.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: arajapak <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/11/26 14:42:36 by arajapak          #+#    #+#              #
#    Updated: 2024/11/26 14:42:48 by arajapak         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/bin/python3
#get prompt enter number
#number is negative display negative
#number is positive display positive
#number equal to zero both positive and negative

number = float(input(" Enter number"))

if number > 0 :
    print("This number is positive")
elif number < 0 :
    print("This number is negative")
else:
    print("This number is both positive and negative")


