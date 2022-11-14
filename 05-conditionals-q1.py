#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Question 1
Write code that asks the user to input a number between 1 and 5 inclusive.
The code will take the integer value and print out the string value. So for
example if the user inputs 2 the code will print two. Reject any input that
is not a number in that range
"""
user_input = int(input('Please enter an integer between 1-5:> '))
if user_input == 1:
    print('one')
elif user_input == 2:
    print('two')
elif user_input == 3:
    print('three')
elif user_input == 4:
    print('four')
elif user_input == 5:
    print('five')
else:
    print('Out of range')
