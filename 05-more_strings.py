#!/usr/bin/env python

# A little more on strings
my_string = 'Python'
print('1)', len(my_string))
print('2)', my_string[0])
print('3)', my_string[1])
print('4)', my_string[0:4])
print('5)', my_string[:4])
print('6)', my_string[-1])
print('7)', my_string.upper())
print('8)', my_string.lower())

word = 'summer'
guess = input('I\'m thinking of a word, can you guess what it is? Hint \
it\'s a season. >>> ')
guess = guess.lower()

if guess == 'summer':
    print('Yes, it\'s Summer, well done!')
elif guess == 'winter':
    print('No, it\'s not Winter. Sorry!')
elif guess == 'autumn':
    print('No, it\'s not Autumn. Sorry!')
elif guess == 'spring':
    print('No, it\'s not Spring. Sorry!')
else:
    print(guess.capitalize(), 'is not a season!')
