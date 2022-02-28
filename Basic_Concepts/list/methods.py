#Methods
#Note: All the list values have a method called index and remembr method is almost similar to function and you can call that
#       method on these pn the list value in the spam 

spam = ['hello', 'hi' , 'howdy', 'heyas']
print(spam.index('hello'))

#We can't call a method by itself, because Python doesn't know which list you're trying to find the index to. That's why we
#have to call it on a value. Rememebr method name comes after the value or the variable that contains a value and a dot. other
#than that it is pretty much exact same as function. each data type has its own set of methods.
print(index('hello'))

#if item doesn't exist in the list it will raise an exception.
print(spam.index("skdjfbjklSFBL"))

#if list contains duplicate it will give index of first item.
spam = ['zophie', 'pokka', 'hokka', 'pokka']
print(spam.index('pokka'))

################################################################################################################################

#append() and insert() list Methods

#Append adds the value to the end of the list
spam = ['cat', 'dog', 'bat']
spam.append('moose')
print(spam)

#insert add the value at certian index
spam = ['cat', 'dog', 'bat']
spam.insert(1, 'chicken')
print(spam)

#Note: this methods returns none value that's why we don't assign it to any variable, for clarification refer below
spam = spam.append('moose')

#Note: append() and insert() are list method they can't be called on values such as strings and integers
egss = 'hello'
print(egss.append('world'))

#################################################################################################################################

#remove() List Method

spam = ['cat', 'dog', 'bat', 'elephant']
spam.remove('cat')
print(spam)

#Note: if we try to remove a value that doesn't exist in the list Python gives us an error
spam.remove('cat')
print(spam)

#del deletes a value specififed at an index
spam = ['cat', 'dog', 'bat', 'elephant']
del spam[0]
print(spam)

#Note: if a value appears multiple times in the list, remove() method will remove it for the first occurence
spam = ['cat', 'dog', 'cat', 'elephant']
spam.remove('cat')
print(spam)

##################################################################################################################################

#sort() List Method

spam = [2,5,1,-7,3.89]
spam.sort()
print(spam)


#sort() method works on list containing strings
spam = ['cat', 'dog', 'bat', 'elephant']
spam.sort()
print(spam)

#reverse sort
spam.sort(reverse = True)
print(spam)

#Note: sort() method doesn't work when list has both strings and numbers
spam = ['cat', 'dog', 'bat', 'elephant', 1,2,3]
spam.sort()
print(spam)

#Note: sort() method uses ASCII-batical order to sort, it means upper case character comes before the lower case character.
spam = ['Alice', 'Bob', 'ants', 'bad', 'cat']
spam.sort()
print(spam)

#Note: if you want true alphabet sorting without neglecting the uppercase and lower case, use the keyword
spam = ['A', 'Z', 'a', 'z']
spam.sort(key = str.lower)
print(spam)
