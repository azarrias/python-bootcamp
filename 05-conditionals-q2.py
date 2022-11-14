#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Question 2
Repeat the previous task but this time the user will input a string and the
code will output the integer value. Convert the string to lowercase first.
"""
user_input = input('Please enter an string between One and five:> ')
user_input = user_input.lower()
if user_input == 'one':
    print(1)
elif user_input == 'two':
    print(2)
elif user_input == 'three':
    print(3)
elif user_input == 'four':
    print(4)
elif user_input == 'five':
    print(5)
else:
    print('Out of range')
