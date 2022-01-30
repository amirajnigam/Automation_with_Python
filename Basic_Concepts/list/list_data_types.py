spam = ['cat', 'bat', 'rat']
print(spam[1])



#lists of lists
spam = [['cat', 'bat'], [10,20,30,40]]
print(spam[0][0])
print(spam[1][1])

#negative index
spam = ['cat', 'bat', 'rat']
print(spam[-1])
print(spam[-2])

#Slices
spam = ['cat', 'bat', 'rat']
print(spam[1:3])
print(spam[:2])
print(spam[1:])

#Assign value in list 
spam = [10,20,30]
spam[1] = 'Hello'
print(spam)

spam[1:3] = ['CAT', 'DOG', 'MOUSE']
print(spam)

#delete a value from list
spam = ['cat', 'bat', 'rat']
del spam[2]
print(spam)

#String and list similarity
spam = 'Hello'
print(list(spam))

#in and not in
print('howdy' in ['hello', 'howdy', 'haja'] )
print(42 in ['hello', 'howdy', 'haja'] )
print('howdy' not in ['hello', 'howdy', 'haja'] )