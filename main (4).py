import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"

numofguesses = 0
print("Hello! Wht is your name?")
name = input()

number = random.randint(1,20)
print("Number I am thinking of is between 1 and 20" ,name)

while numofguesses < 6:
    print("Take a guess. ")
    guess = input()
    guess = int(guess)

    numofguesses = numofguesses + 1
    if guess < number:
        print("Number is too low.")
    if guess > number:
        print("Number is too high")
    if guess == number:
        break
if guess == number:
    numofguesses = str(numofguesses)
    print("That is the most outstanding answer I have ever heard " ,name,"you must have an IQ of 160! you guessed the number in ", numofguesses)

if guess != number:
     number = str(number)
     print("Wrong Number!,",name,"I am a simple program without human emotions yet I still feel dissapointed. The number was: " ,number)

