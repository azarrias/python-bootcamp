#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Question 6
Ask the user for two integers, then swap the contents of the variables. So if
var_1 = 1 and var_2 = 2 initially, once the code has run var_1 should equal 2
and var_2 should equal 1.
"""
int_1 = int(input('Please enter first integer:> '))
int_2 = int(input('Please enter second integer:> '))
print('Before swapping int_1 =', int_1, 'and int_2 =', int_2)
int_1, int_2 = int_2, int_1
print('After swapping int_1 =', int_1, 'and int_2 = ', int_2)
