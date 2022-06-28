#Escape character : it lets you use characters that are otherwise impossible to put into a string.

#problem
#print('That is Alice's cat') #Python will think strings ends at alice and string after ' is invalid code

#use double quote or escape character instead
print("That is Alice's cat")
print("That is Alice\'s cat")

print('Hello there\nHow are you\nI\'m fine')

#############################################################################################################
#raw string

print(r'Hello')
print(r'That is carol\'s cat')

#############################################################################################################

#multiline strings with triple quotes

print("""Dear Alice,
how are you,
everything is good at my end,
hope to see you soon""")

############################################################################################################

#Similarities between Strings and lists

spam = 'Hello world'

print(spam[0]) #pick indexes
print(spam[1:5]) #slicing
print(spam[-1])
print('Hello' in spam)
