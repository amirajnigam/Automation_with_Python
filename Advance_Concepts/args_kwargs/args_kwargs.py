#*args and **kwargs tutorial
#*vars and **kvars tutorial

#Note the name doesn't matter only tha "*" matters

def function_1(*args):                                                                              # *args is used to denote variable numbers of argument and is of tuple type
    #print(type(args))                                                                              #Tuple data type so that we can't change its value.
    if(len(args) == 3):
        print("The name of student is", args[0], "and age is", args[1], "and rollno is", args[2])
    else:
        print("The name of student is", args[0], "and age is", args[1])


def printmarks(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():                                                               # items() is a dictionary function if we run on dictionary it gives key and values of dict
        print(key,value)






def master(normal, *args, **kwargs):
    print(normal)
    
    for i in args:
        print(i)
    
    for key,value in kwargs.items():
        print(key,value)



lis = ["harry", 22, 3894579]
#function_1(*lis)
#function_1("harry", 22, 3455874)

marklist = {"harry": 100, "Ron": 78, "Hermoine": 98, "Snape": 85, "Hegrid": 65}

#printmarks(**marklist)

master("normal arg", *lis, **marklist)