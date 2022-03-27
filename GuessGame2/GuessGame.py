import random
import time

a = int(input("Pick a number between 1-1000 : "))
x,y = 1,1000
while True:
    time.sleep(1)
    b = random.randint(x,y)

    if b > a:
        print("Computer guessed: ",b,"\nToo high")
        y = b-1

    if a > b:
        print("Computer guessed: ",b,"\nToo low")
        x = b+1

    if a == b:
        print("Computer guess is right!","The number was",b)
        break
    