import random

#computer comes up with secret number and user guess it
def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    tries = 0
    while guess != random_number:
        tries+=1
        guess = int(input(f"Please enter a guess betwee 1 and {x}: "))
        while guess < 1 or guess > x:
            guess = int(input(f"Please enter a guess betwee 1 and {x}: "))         
        if guess > random_number:
            print("Too high!")
        elif guess < random_number:
            print("Too low!")
    print("You have guessed " +str(random_number) +" after "+ str(tries) + " tries")
    
guess(10)
