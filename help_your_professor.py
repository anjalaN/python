#!/usr/bin/env python3
import math

class_3B = {
"marine": 18,
"jean": 15,
"coline": 8,
"luc": 9
}

class_3C = {
"quentin": 17,
"julie": 15,
"marc": 8,
"stephanie": 13
}

number1 = sum(class_3B.values())
number2 = len(class_3B.keys())

number3 = sum(class_3C.values())
number4 = len(class_3C.keys())


result1 = number1/number2
result2 = number3/number4

print("Average for class 3B: ", result1) 
print("Average for class 3C: ", result2) 