try :
    file = open("this.txt", 'r')

except EOFError as e:
    print("eof error")
except IOError as e:
    print("We can handle this error")

finally:
    print("This will be printed irrespective of the exception occurence")