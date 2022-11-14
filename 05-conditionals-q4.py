#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Question 4
Ask the user to input their name. Check the length of the name. If it is
greater than 5 characters long, write a message telling them how many characters
otherwise write a message saying the length of their name is a secret
"""
name = input('Please enter your name:>')
name_len = len(name)
if name_len > 5:
    print('Your name contains', name_len, 'characters.')
else:
    print('I\'m not telling you the length of your name.')
