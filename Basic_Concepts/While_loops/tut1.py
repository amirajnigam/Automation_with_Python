# spam = 0
# while spam <5:
#     print("Hello World")
#     spam = spam + 1

#################################################################################################################

#Example of input validation -> A good example of asking user until they enter a valid input
# name = ''
# while name != 'your name':
#     print("Please Enter your name")
#     name = input()
# print("Thank you")

##################################################################################################################

#Infinite Loop
# while True:
#     print("Hello!")

##################################################################################################################

#Break statement
# name = ''
# while True:
#     print("Please Enter your name")
#     name = input()
#     if name == 'your name':
#         break
# print("Thank you")

##################################################################################################################

#Continue Statement
spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue
    print('spam is ' + str(spam) )


"""""
 * When the execution reaches the end of a "while" statement's block, it jumps back to the start to re-check the condition.
 * You can press ctrl-c to interrupt an infinite loop. This hotkey stops Python programs.
 * A "break" statement causes the execution to immediately leave the loop, without re-check the condition.
 * A "continue" statement causes the execution to immediate jump back to the start of the loop and re-check the condition.
 """