
class Employee:
    
    increment = 1.5                                                
    no_of_employee = 0

    def __init__(self, fname, lname, salary):    
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

class Programmer(Employee):                                                                 #Progammer class has inherited all the variables and method of Employee class
    #We are changing the constructor for the Programmer class
    def __init__(self, fname, lname, salary, proglang, exp):
        super().__init__(fname, lname, salary)                                              #super.__init__() call the constructor(__init__) of the Parent class
        self.proglang = proglang
        self.exp = exp

    def increase(self):                                                                                        
        self.salary = int(self.salary * (self.increment + 0.2))  


harry = Programmer('harry','Jakson', 99000, 'Python','5 years')
print(harry.exp)
print(harry.proglang)
help(Programmer)                                                                              #help will give all the details of the class                                                        