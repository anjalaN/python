#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    family_affairs.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: arajapak <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/09 16:23:14 by arajapak          #+#    #+#              #
#    Updated: 2024/12/09 16:23:18 by arajapak         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
#create dictionary
def find_the_redheads(upont_family):
    redhead = list(filter( lambda name_color: name_color[1]=="red", dupont_family.items()))
    return [name for name, color in redhead]

#donne des information
dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}
#appelle dictionary
print(find_the_redheads(dupont_family))
