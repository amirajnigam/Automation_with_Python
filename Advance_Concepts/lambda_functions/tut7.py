"""

Lamba are called one luine functions or Anonymus functions

Syntax:
lambda argument : manipulate(argument)

"""


# def add(a,b):
#     s = a+b
#     return s
# print(add(4,6))


add = lambda x,y: x+y
print(add(4,12))

#use of lambda functions

a = [(1,2), (4694,568), (555,34)]
a.sort(key = lambda x:x[0])                 #sort the list on first element of the tuple...........key is an optional parameter in sort function
print(a)

