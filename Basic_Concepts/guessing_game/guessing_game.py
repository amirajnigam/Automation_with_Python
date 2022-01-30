import random
print("Hello, what is you name!")
name = input()
secretnumber = random.randint(1,20)
print('Well ' + name + ',I am thinking of a number between 1 and 20')

for guessTaken in range(1,7):
    print("Take a guess")
    guess = int(input())

    if guess < secretnumber:
        print("Your guess is too low.")
    elif guess > secretnumber:
        print('Your guess is too high')
    else:
        break #This condition is for the correct guess!

if guess == secretnumber:
    print("Good job " + name + 'you guessed my number in ' + str(guessTaken) + 'guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretnumber))
