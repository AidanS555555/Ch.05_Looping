'''
COIN TOSS PROGRAM
-----------------
1.) Create a program that will print a random 0 or 1.
2.) Instead of 0 or 1, print heads or tails. Do this using if statements. Don't select from a list.
3.) Add a loop so that the program does this 50 times.
4.) Create a running total for the number of heads and the number of tails and print the total at the end.
'''
#import requests
import random
x=0
y=0
coin_side= random.randint(0,1)

for i in range(50):
    coin_side = random.randint(0, 1)
    if coin_side==1:
        print("The coin landed on heads")
        x+=1

    else:
        print("The coin landed on tails")
        y+=1



print("This is the number of tails:", y)
print("This is the number of heads:", x)














