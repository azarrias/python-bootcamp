#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Question 5
Ask the user for two integers between 1 and 20. If they are both greater than
15 return their product. If only one is greater than 15 return their sum, if
neither are greater than 15 return zero
"""
int_1 = int(input('Please enter an integer between 1-20:> '))
int_2 = int(input('Please enter another integer between 1-20:> '))

if int_1 > 15 and int_2 > 15:
    print(int_1 * int_2)
elif int_1 > 15 or int_2 > 15:
    print(int_1 + int_2)
else:
    print(0)
