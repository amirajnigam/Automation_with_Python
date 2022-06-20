#like a list dictionary is collection of many values but unlike list indexes, indexes of dictionary can use many different data types not just integers
# indexes for dictionary are called keys and a key with its associated value is called a key value pair

mycat = {'size': 'fat', 'color': 'black', 'disposition': 'loud' }
print(mycat['size']) # how to access the value of dict

print('My cat has ' + mycat['color'] + ' fur') #string concationation

##########################################################################################################################################################

#dictionary are unordered

spam = {12345: 'luggage combination', 42: 'The Answer'}
cheese = { 42: 'The Answer', 12345: 'luggage combination'}

print(spam == cheese) #dict hjas no order

#print(cheese['sophie']) #key doesn't exist - keyerror

print(42 in cheese)
print(42 not in cheese)

#dictionary are mutable like list, variables hold the references to dictionary values, variable don't actually hold the dictonary value itself

#########################################################################################################################################################

#Dictionaryu methods keys(), values(), items()

eggs = {'name': 'zophie', 'species': 'cat', 'age': 8}

print(list(eggs.keys()))
print(list(eggs.values()))
print(list(eggs.items())) #it returns 2 items tuple
print(eggs.values()) # this generates dict_values, so actually we have to pass it to list function and it will return a list value

for k in eggs.keys():
    print(k)

for v in eggs.values():
    print(v)

for k,v in eggs.items():
    print(k,v)

# or we can assign tuple values from items() to a single variable

for i in eggs.items():
    print(i)

#checking keys and value in dict

print('cat' in eggs.values())

#########################################################################################################################################################

# get() dictionary method

#print(eggs['color']) # check key exist in dict, if not then it will give a key error and program will crash

#to avoid that we use below technique

if 'color' in eggs:
    print(eggs['color'])

#but it is to lengthy, here get() comes in handy, get has 2 parameters,1st is key and 2nd is if the key doesn't exist then return the 2nd parameter

print(eggs.get('age', 0))
print(eggs.get('color', 'color doesnt exist in the list'))

picnicitems = {'apples' : 5, 'cups': 2}
print("I am bringing " + str(picnicitems.get('napkins', 0)) + ' to the picnic')

######################################################################################################################################################

#opposite of get() is setdefault() dict method

eggs = {'name': 'zophie', 'species': 'cat', 'age': 8}

if 'color' not in eggs:
    eggs['color'] = 'black'

print(eggs)

#easy way of doing it

eggs = {'name': 'zophie', 'species': 'cat', 'age': 8}

eggs.setdefault('color', 'black') #if color was not in dictionary then add the key value pair to it
print(eggs)

eggs.setdefault('color', 'orange') # but this will not do anythings because color:black key value pair already exist in dict
print(eggs)