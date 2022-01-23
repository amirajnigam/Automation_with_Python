'''''
def div42by(divideby):
    try:
        return 42/divideby
    except ZeroDivisionError:
        print("Error: You try to divide by zero")

print(div42by(42))
print(div42by(12))
print(div42by(0))                   #Remember: function that has no return value returns None
print(div42by(1))

'''
#Input validation example

print('How many cats do you have?')
numCats = input()

try:
    if int(numCats) >= 4:
        print('That is lot of cats')
    else:
        print('That is not many cats')
except ValueError:
    print('You did not enter a number!!')
        