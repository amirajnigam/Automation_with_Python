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