#!/usr/bin/env python3
import requests
city = input("input the city name :")
print(city)
print("dispayweather report" +city)

url = 'https://wttr.in/{}' .format(city)
res = requests.get(url)
print(res.text)