import os

def mostimpfunction():
    print("harry is a coder")

print(__name__)                                                         #The value of__name__ will be __main__ if it is called from the same file, but it will print tut1a if tut1b.py is run 


def main():
    print(os.listdir("/"))                                              #Will give the current and other diretory details
    print("Harry is great and he is the king of the US" )

if(__name__  == "__main__"):
    main()




#The reason fior writing print statement "Harry is great.......the US" in seperate main function so that when we want to print these lines after running tut1b.py we can do that. if it was mentioned in if(__name__ == "__main__") there was no other way to print these line while running tut1b.py

#For more detailed explanation watch the tutorial -> https://www.youtube.com/watch?v=qzbZIxnFKPc&list=PLu0W_9lII9aiJWQ7VhY712fuimEpQZYp4&index=1