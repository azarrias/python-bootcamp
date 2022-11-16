#!/usr/bin/env python

# Ask the user for the radius of a circle and then print the area
print('[Q1]')
radius = float(input('Please enter the circle radius: '))
pi = 3.14159
area = pi * radius ** 2
print('You entered', radius, 'the area of the circle is', area)
print()

# Convert fahrenheit to celsius
print('[Q2]')
far = float(input('Please enter the temperature in Fahrenheit: '))
cel = (far - 32) * 5 / 9
print(far, 'Fahrenheit in Celsius is', cel)
print()

# Obtain the sum of two integers
print('[Q3]')
num_1 = int(input('Please enter the first number: '))
num_2 = int(input('Please enter the second number: '))
print('The sum of ' + str(num_1) + ' and ' + str(num_2) + ' is ' + str(num_1 + num_2))
print()

# Obtain the product of two integers
print('[Q4]')
num_1 = int(input('Please enter the first number: '))
num_2 = int(input('Please enter the second number: '))
product = num_1 * num_2
print('The product of', num_1, 'and', num_2, 'is', product)
print()

# Bob, Ann, Jane and Ashwin want to order pizza - they know they will each eat
# 4 slices of pizza. The local pizza shop sells pizzas of only 6 slices
# What is the minimum number of pizzas needed - Use floor division
print('[Q5]')
total_slices = 4 * 4
number_of_pizzas = (total_slices + 5) // 6
slices_left = number_of_pizzas * 6 - total_slices
print('Number of pizzas required is', number_of_pizzas, 'there will be',
      slices_left, 'remaining slices.')
print()