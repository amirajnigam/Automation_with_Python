import bisect

number = 5
a = [1,2,4,6,7,8,23,456]
print(a)

#bisect gives the index in the list where we want to insert the element after which the list remain sorted
print(bisect.bisect(a,number))


#insort will insert the element at specific location after which the list remain sorted.
bisect.insort(a, number)
print(a)