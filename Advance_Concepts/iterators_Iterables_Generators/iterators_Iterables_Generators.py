"""


Iterable - its an object in which can give us iterator
Iterator - its an  object in which next method is defined.
Iteration - 
Generator - Generator are iterators which can generate value only one time

"""

def gen(n):
    for i in range(n):
        yield i                                                             #yield is a keyword which is used to yield a number i but not generating a number i at here.


# print(gen(100000))                                                        #gen function has created an object at some memory location, it has not consumed ram and we can use this to generate this number(1000), like its generating values on the fly
# for i in gen(1000):
#     print(i)


ob1 = gen(4)
# print(next(ob1))
# print(next(ob1))
# print(next(ob1))
# print(next(ob1))
# print(next(ob1))
# print(next(ob1))
# print(next(ob1))
# print(next(ob1))


# num = 345
# for i in num:
#     print(i)                                                                #it will give an error because integer is not an iterable


num = "harry"
# for i in num:
#     print(i)

iter1 = iter(num)                                                               #the iter() function returns an iterator for the given object, the iter() function xcreates an object which can be iterated one element at a time
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))