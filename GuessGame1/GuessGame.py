import random

print("Welcome To My Guess Game 1")

a = random.randint(1,100)

lives = 6
while True:
    b = int(input("Guess a nuber between 1-100 (including 1 and 100): "))

    if b > a:
        print("Your guess is too high, Try again.")
        lives -= 1
        print("remaining lives: ",lives)

    elif a > b:
        print("Your guess is too low, Try again.")
        lives-=1
        print("remaining lives: ",lives)
    
    
    if lives == 0:
        print("You are out of lives! The number was: ",a)
        break

    if a == b:
        print("You guessed The number: ",a)
        break

    



