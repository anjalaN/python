#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    age.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: arajapak <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/11/29 16:10:36 by arajapak          #+#    #+#              #
#    Updated: 2024/11/29 16:10:36 by arajapak         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
#user enter age
#display current age
#current age + 10 loop
age = int(input("Please tell me your age: "))

#print("You are currently", age, "years old.")

#print("In 10 years, you'll be", age+10, "years old.")
#print("In 10 years, you'll be", age+20, "years old.")
#print("In 10 years, you'll be", age+30, "years old.")

for a in range(10,40,10):
    print("In 10 years, you'll be", age+a, "years old.")
    
