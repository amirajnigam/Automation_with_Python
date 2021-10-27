#try and except is used when if some code doesn't work then to handle its exception we put the code in except block and try to run it if it doesn't work then throw the exception.
#Error and exception are two different things if an error is occured then program will not rexecute further wheras in try and error program will try to execute the condition in try block and if doesn't work then it will go in exception block and do the desired operation and program will execute further.


try:
    open("this.txt")
except Exception as e:                                                      #You can give anything such as e, error, amu, falana_dhikana
    print(e)

print("program zibnda hai")