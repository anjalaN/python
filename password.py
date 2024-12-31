# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    password.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: arajapak <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/11/26 14:43:50 by arajapak          #+#    #+#              #
#    Updated: 2024/11/26 14:44:03 by arajapak         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
#!/bin/python3
#get password with prompt
#password correct display ACCESS GRANTED
#password incorrect display ACCESS DENIED

password = "Python is awesome"

newPassword = input("Enter your password")

if password == newPassword :
     print("ACCESS GRANTED")
else :
     print("ACCESS DENIED")
