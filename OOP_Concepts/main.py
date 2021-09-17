#######################################################################

#not a proper use of OOP concepts

"""class Employee:
    pass

harry = Employee()                    #object creation
rohan = Employee()

harry.fname = "harry"
harry.lname = "jakson"
harry.salary = "44000"

rohan.fname = "rohan"
rohan.lname = "das"
rohan.salary = "44000"

print(harry, rohan) """

#######################################################################


#How to use class efficiently

class Employee:
    def __init__(self, fname, lname, salary):    #constructor __init__, it take first argument as self, self is the first object which we are talking about. When an object is created this function will run by default
        self.fname = fname                      #self.fname is class variable on LHS, whereas fname on RHS is the arguemtn taken by function, same as for below
        self.lname = lname
        self.salary = salary


harry = Employee('harry', 'jakson', 44000)
rohan = Employee('rohan', 'das', 44000)

print(harry.fname, rohan.fname)



# Class is a template(for example consider template for Power point which is same for every presentation but each presentation is different)
# We can mention pass if we don't want to mention anything in class, it will not give an error
# Explanation consider the class employee created above as template of Power point and when we want to give different presernation we will use the same template
#we will create an object harry = Employee('harry', 'jakson', 44000) and we want to fill the data on object automatically in template which is done by constructor