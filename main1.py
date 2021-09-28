''' A blueprint for a house design is like a class description. 
    All the houses built from that blueprint are objects of that class.
    A given house is an instance.
'''

class Employee:

    increment = 1.5                                                 #class variable
    no_of_employee = 0

    def __init__(self, fname, lname, salary):    
        self.fname = fname                      
        self.lname = lname
        self.salary = salary
        self.increment = 1.4
        Employee.no_of_employee += 1


    def increase(self):                                             #While calling this function/method if we dont give any argument in callee function then it will take self as 1 argument
        self.salary = int(self.salary * self.increment)             #self.increment will look for icrement variable in instance as well as class variable
        #self.salary = int(self.salary * Employee.increment)        #Employee.increment will look for calss variable


print(Employee.no_of_employee)
harry = Employee('harry', 'jakson', 44000)
rohan = Employee('rohan', 'das', 44000)
print(Employee.no_of_employee)

print(harry.salary)
harry.increase()                                                    #Whenver we call call a function with an object then a self will automatically will go in the function argument
print(harry.salary)


#print(harry.__dict__)                                               #__dict__ will list all the variable for the harry(object) instance personal variables
#harry.yearly_leave = 10
#print(harry.__dict__)

#print(Employee.__dict__)                                            #This will list all the variables for the Employee class