'''
Builtin-function: print(), input(), len( )


'''


import random

print(random.randint(1,10))             #random is the module name, randint is the function inside the module


import random, sys, os, math            #we can enter multiple module names seperated by commas.

from random import *                    #This command will import all the functions from random module and we don't have to write module name while calling the function but not recommended

print(randint(1,10))



import sys
print("Hello")

#sys.exit()                              #This function exit the program at any instance called in the program

print("Good Bye")

import pyperclip

pyperclip.copy("Helloworld")
print(pyperclip.paste())





# You can import modules and get access to new functions.
# The modules that come with Python are called the standard library, but you can also install third-party modules using the pip tool.
# The sys.exit() function will immediately quit your program.
# The Pyperclip third-party module has copy() and paste() functions for reading and writing text to the clipboard().