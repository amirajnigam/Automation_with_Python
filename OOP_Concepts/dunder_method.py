
class Employee:
    
    increment = 1.5                                                
    no_of_employee = 0

    def __init__(self, fname, lname, salary):                                   #dunder __init__ is a special method/constructor 
        self.fname = fname                      
        self.lname = lname
        self.salary = salary
        Employee.no_of_employee += 1


    def increase(self):                                                                                        
        self.salary = int(self.salary * self.increment)             

    @classmethod                                                     
    def change_increment(cls,amount):                                      
        cls.increment = amount

    @classmethod                                                    
    def from_str(cls, empl_string):                                    
        fname,lname,salary = empl_string.split("-")
        return cls(fname, lname, salary)                            

    @staticmethod
    def isopen(day):
        if day =="sunday":
            return False
        else:
            return True

    def __add__(self, other):                                                       #dunder method or magic function
        return self.salary + other.salary

    def __repr__(self):                                                             #dunder method or magic function
        return 'Employee({},{},{})'.format(self.fname, self.lname, self.salary)

    def __str__(self):                                                              #dunder method or magic function
        return 'The name of employee is {}'.format(self.fname)


harry = Employee('harry', 'jakson', 99000)
rohan = Employee('rohan', 'agarwal', 1000000 )

#sprint(harry + rohan)

#print(repr(harry))

print(str(harry))

