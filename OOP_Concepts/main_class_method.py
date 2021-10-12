class Employee:
    
    increment = 1.5                                                 #class variable
    no_of_employee = 0

    def __init__(self, fname, lname, salary):    
        self.fname = fname                      
        self.lname = lname
        self.salary = salary
        Employee.no_of_employee += 1


    def increase(self):                                             
        self.salary = int(self.salary * self.increment)             

    @classmethod                                                     #decorator
    def change_increment(cls,amount):                                      #class method - it takes an entire class as an argument, cls denotes class as an argument
        cls.increment = amount


harry = Employee('harry', 'jakson', 44000)
rohan = Employee('rohan', 'das', 74000)


print(harry.salary)
Employee.change_increment(3)
harry.increase()
print(harry.salary)


#Why we need class method?
#Ans: Because we don't want to pass the object to the fucntion just because we want to change one variable(increment) of the class. So, we created one method (change_increment()) which doesn't take object as
#     argument, and simply take class as an argument and update its variable.