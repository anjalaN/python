#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    scope_that.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: arajapak <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/06 16:54:01 by arajapak          #+#    #+#              #
#    Updated: 2024/12/06 16:54:13 by arajapak         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
#only test local scope

def add_one():
    x=0
    x=x+1  

i=0
print(i)
add_one()
print(i)


