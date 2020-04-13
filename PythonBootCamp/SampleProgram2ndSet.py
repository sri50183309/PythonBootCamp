# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 06:53:49 2020

@author: srira
"""


import math
print(math.pi)

#import webbrowser
#webbrowser.open_new("http://www.google.com")

capitals={"France":"Paris",
          "India":"Delhi"}

print(capitals["India"])

capitals["USA"] = "Washington"

print(capitals)

for country,city in capitals.items():
    print(f'The capital of {country} is {city}')
    
print(capitals.keys())

story_string = """
My name is Sriram and i am in Novi. I have 2 kids and my family is very happy one.
"""
letter_count = {}

for letter in story_string:
    letter_count[letter] = letter_count.get(letter,0) + 1
    
print(letter_count.items())

import matplotlib.pyplot as plt

a,b = zip(*letter_count.items())

print(a)
print(b)

plt.bar(a, b)
plt.show()