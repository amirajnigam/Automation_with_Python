class Employee:
    
    increment = 1.5                                                 #class variable
    no_of_employee = 0

    def __init__(self, fname, lname, salary):    
        self.fname = fname                      
        self.lname = lname
        self.salary = salary
        Employee.no_of_employee += 1


    def increase(self):                                             #This self here take the object which is returned by the class as argument                                            
        self.salary = int(self.salary * self.increment)             

    @classmethod                                                     
    def change_increment(cls,amount):                                      
        cls.increment = amount

    @classmethod                                                    #Alternative constructor
    def from_str(cls, empl_string):                                    #from_str function will return an object and it will assign to lovish
        fname,lname,salary = empl_string.split("-")
        return cls(fname, lname, salary)                            #cls is Employee


harry = Employee('harry', 'jakson', 44000)                          #class Employee returns an object

lovish = Employee.from_str("lovish-jakson-76000")

rohan = Employee('rohan', 'das', 74000)


print(lovish.fname)
print(lovish.lname)
print(lovish.salary)


#__init__ is a orignal constructor, but we can use class method function as alternate constructor.