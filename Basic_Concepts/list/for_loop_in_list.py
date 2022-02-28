#for loop
for i in range(4):
    print(i)

#or 

for i in [0,1,2,3]:
    print(i)

##########################################################################################

#list function
print(list(range(4)))  # This can be useful if we need collection of intwegers in the list

print(list(range(0,100,2))) #print from 0 to 100 after every 2 numbers

##########################################################################################

#for i in range(len(somelist)):

supplies = ['pen', 'staples', 'binders']
for i in range(len(supplies)):
 print('Index ' + str(i) + ' in supplies is ' + supplies[i])

###########################################################################################

#Multiple assignment

cat = ['fat', 'orange', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]

print(size, color, disposition)

#or instead of assigning each element to the list we can assign as mentioned below

size, color, disposition = cat
print(size, color, disposition)

#miltiple assignment on the right
size, color, disposition = 'skinny', 'black', 'quiet'
print(size, color, disposition)

#can be used for swaping the variable
a = "AAA"
b = "BBB"
a,b = b,a
print(a,b)

#############################################################################################

#Augmented assignment operators

spam = 42
spam = spam + 1
#or
spam += 1
print(spam)