'''

List Comprehension
Dictionary Comprehension
Set Comprehension
Generator Comprehension 

'''


#list
list_1 = [1,3,5,67,2,56,24,89,31,56,89,90,345,150]
divide_by_3 = []
for item in list_1:
    if item%3 == 0:divide_by_3.append(item)

print("Without using list comprehension", divide_by_3)
print("Using list comprehension", [item_2 for item_2 in list_1 if item_2%3 ==0])

#dictionary
dict1 = {'a':45, 'b':65, 'A': 5}
print({k.lower():dict1.get(k.lower(), 0) + dict1.get(k.upper(), 0) for k in dict1.keys()})                          #read from right to left

#set
squared ={x**2 for x in [1,2,3,4,5,2,3,5,7,2,2]}
print(squared)



gen = (i for i in range(56) if i%3 == 0)                                                                            #gen has not allocated any memory here, it has initialized an object, and when we are running a for loop on it, it is generating values on the fly. with this we are saving ram but program takem ore time to execute                                         
for item in gen:
    print(item)
