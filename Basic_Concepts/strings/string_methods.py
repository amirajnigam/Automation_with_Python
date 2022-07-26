# upper() and lower()

spam = 'Hello World!'
print(spam.upper())
print(spam.lower())

print(spam) #it will print the original letters

spam = spam.upper() #to permanently change the letter
print(spam)

######################################################################################################

#isupper() and islower()

spam = 'Hello World!'
print(spam.islower())
print(spam.isupper())

spam = '' # a string must contain atleast one character
print(spam.islower())
print(spam.isupper())

spam = '12345' # atleast one letter required
print(spam.islower())
print(spam.isupper())

print('Hello'.upper().isupper()) #chain method

#other methods -> isalpha(), isalnum(). isdecimal(), isspace(), istitle()

########################################################################################################

#startswith() and endswith()

print('Hello world!'.startswith('H'))
print('Hello world!'.startswith('Hell'))
print('Hello world!'.endswith('!'))
print('Hello world'.endswith('vs'))

########################################################################################################

#join() and split9)
 
print(','.join(['cats', 'rats', 'bats']))
print(' '.join(['cats', 'rats', 'bats']))
print('\n'.join(['cats', 'rats', 'bats']))

print('My name is Simon'.split())  #splits on white space characters
print('My name is Simon'.split('m')) #split on m

#######################################################################################################

#ljust() and rjust() and center()

print('Hello'.rjust(10)) #it will add space to make the total string length to 10
print('Hello'.ljust(10))

print('Hello'.rjust(10, '*')) 
print('Hello'.ljust(10, '*'))

print('Hello'.center(20))
print('Hello'.center(20, '*'))

######################################################################################################

#strip(), rstrip() and lstrip()

spam = 'Hello'.rjust(10)
print(spam.strip()) #strip of the white space

print('     x    '.strip())
print('     x    '.lstrip())
print('     x    '.rstrip())

#can be used to remove characters instead of white space

print('SpamSpamBaconSpamEggsSpamSpam'.strip('Spam'))

spam = 'Hello there'
print(spam.replace('e','XYZ'))

##################################################################################################

#Pyperclip Module -> it will copy and paste string to clip board
 
import pyperclip

pyperclip.copy('Hello!!!!!!')
pyperclip.copy('Hello!!!!!!')