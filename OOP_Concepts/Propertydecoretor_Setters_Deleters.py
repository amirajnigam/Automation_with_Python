
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

    @property                                                       # @property means Property decorator which means see email function as attribute not as function
    def email(self):
        if self.fname == None:
            return "Email not set"
        else:
            return self.fname + '.' + self.lname +'@email.com'

    @email.setter                                                    #setter set the things 
    def email(self, given_email):
        name_list = given_email.split('@')[0].split('.')
        self.fname = name_list[0]
        self.lname = name_list[1]

    @email.deleter
    def email(self):
        self.fname = None                                           #In Python OOP delete is not used instead none is used to delete something
        self.lname = None
 
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

if __name__ == '__main__':
    harry = Employee('harry', 'jakson', 99000)
    rohan = Employee('rohan', 'agarwal', 1000000 )
    print(harry.email, rohan.email)
    rohan.lname = 'khanna'
    print(rohan.email)
    rohan.email = 'khanna.rohan@email.com'                          #if we want to change theemail ID then setter is used
    print(rohan.email)

    del rohan.email                                                 #if we want to delete the email ID then deleter is used.
    print(rohan.email)


#Totorial Link = https://www.youtube.com/watch?v=zZtiJJRXb34&list=PLu0W_9lII9ahfRrhFcoB-4lpp9YaBmdCP&index=9