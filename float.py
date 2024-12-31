#!/usr/bin/env python3
from decimal import *
number = input("Give me a number: ")
if number.replace(".", "", 1).isdigit():
    if "." in number:
        number = float(number)
        if number.is_integer():
            print("This number is an integer. ")
        else:
            print("This number is a decimal.")
    else:
        print("This number is an integer.")
else:
    print("This number is not valide.") 


