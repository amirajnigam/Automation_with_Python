from hashlib import new


print(list('Hello'))

name = 'Zophie'
print(name[0])
print(name[1:3])
print(name[-1])
print('Zo' in name)
print('xxx' in name)

for letter in name:
    print(letter)


############################################################################################################################

#Mutable and Immutable Data Types

#strings are immutable i.e. it cannot be changed

name = 'Zophie the cat'
print(name[7]) # we can access the item from the string

#name[7] = 'X' #but we can't assign

###########################################################################################################################

#Creating new strings from Slices
#Proper way to modify a string is to create a new string using slices

name = 'Zophie a cat'
newName = name[0:7] + 'the' + name[8:12]
print(newName)

#############################################################################################################################

#References(whatch video again if confused)

#Variables stores strings and integer values
spam = 42
cheese = spam
spam = 100
print(spam)
print(cheese)

#in abopve spam will print 100 and cheese will print 42, but list doesn't work like that

#when we assign a list to variable we actually assign a list reference to a variable and referencesa a value that points to some bit of data like a list.

spam = [0,1,2,3,4,5]
cheese = spam
cheese[1] = 'Hello!'
print(cheese) # this will print the updated list with hello
print(spam) # this will also print the updated list with hello

#passing list in function call

def eggs(cheese):
    cheese.append('Hello')

spam = [1,2,3]
eggs(spam)
print(spam)

#here when we are passing spam to eggs function, we are passing the reference to the spam list and the function is updating a list stored in the reference location. henceforth, when we are printing spam outside of function it is printing updated list because spam holds the refernence to the list
#remember for mutable data type such as list we are actually storing a reference to that list inside of a variable and when we are calling a fucntion or do an assignment we are actually coopying a reference to it.

########################################################################################################################

#deepcopy module
#it actually creates a brand new list that just happens to have all the same values here and it returns a reference to this new list

import copy

spam = ['A', 'B', 'C']
cheese = copy.deepcopy(spam)
cheese [1] = '42'
print(cheese)
print(spam)

######################################################################################################################

#Line continuation

spam = ['apples',
        'oranges',
        'bananas',
        'cats']
#or

print('Four score and seven' + \
        ' years ago')
#same

print('Four score and seven' + ' years ago')