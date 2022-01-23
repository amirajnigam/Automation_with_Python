spam = 42  #global variable           Global scope

def eggs():
    spam = 42 #local variable        local scope

print('Some code here')              #Global scope       

#global and local variable
def spam():
    eggs = 'Hello'                   #local variable
    print(eggs)

eggs = 42                            #global variable
spam()
print(eggs)


#Assign a new value to a global variable from inside a function
def spam():
    global eggs
    eggs = 'Hello'                  
    print(eggs)

eggs = 42                           
spam()
print(eggs)
