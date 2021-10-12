
#static function - if we don't want the variables from class and ionstance then we make static function. In this function it will not take class and self as argument

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
        
print(Employee.isopen("sunday"))

#or

shubham = Employee('shubham', 'jakson',99000)
print(shubham.isopen('monday'))
