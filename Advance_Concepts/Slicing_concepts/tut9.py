list1 = [3,4,5,7,8,9,34,32,56,3]

#no. of elementsio n the list: 3-1 = 2......easy logic to remember
#index 1 will be present in the list, whereas index 3 will not be present, index will be less than 1
print(list1[1:3])

#if we give a number larger than the list elements then Python36 and above will not thrwo the error for that, it will print till last element
print(list1[1:71])


#below mentioned first statement will print from index 1 to last element. second statement will print from index 0 to 4]
print(list1[1:])
print(list1[:5])


#Negative Slicing: -1 is the index of the last element of the list and index increases backward..-2, -3.
print(list1[-2: -5])            #it will print nothing
print(list1[-2: 5])             #it will print nothing
print(list1[-5: -2])            #it will print elements from index -3, -4 & -5
print(list1[-2:])               #it will print element at index -1 and -2

print(list1[:-2])               #this and below mentioned print statement wil print the same list.
print(list1[0:8])


#step in list
print(list1[::2])               #it will print elements by jumping 2 elements starting from index 0
print(list1[::3])               ##it will print elements by jumping 3 elements starting from index 0
print(list1[::1])               #it will print the exact same list
print(list1[::-1])              #it will print the list from index -1, also useful for reversing the list
print(list1[::-2])              #it will print the list from index -1 and jump 2 elemets at a time