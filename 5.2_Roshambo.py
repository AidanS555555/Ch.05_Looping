'''
ROSHAMBO PROGRAM
----------------

Create a program that randomly prints 1, 2, or 3.
Expand the program so it randomly prints rock, paper, or scissors using if statements. Don't select from a list.
Add to the program so it first asks the user their choice as well as if they want to quit.
(It will be easier if you have them enter 1 for rock, 2 for paper, and 3 for scissors.)
Add conditional statements to figure out who wins and keep the records
When the user quits print a win/loss record

'''
import random
x=0
y=0
rock=1
paper=2
scissors=3
b=0

for i in range(500):
    quit = str(input("Do you want to quit? (y/n)"))
    if quit == y:
        b += 1
    if b==1:
        print("You are done")
        break
    print("1 equals rock, 2 equals papaer, 3 equals scissors")
    choice=int(input("Enter a number between 1 and 3"))
    compchoice=random.randint(1,3)
    if choice==compchoice:
        print("It's a tie")
    elif choice==1 and compchoice==3:
        print("You win!!")
        x+=1
    elif choice==1 and compchoice==2:
        print("You lose")
        y+=1
    elif choice==2 and compchoice==1:
        print("You win!!")
        x+=1
    elif choice==3 and compchoice==2:
        print("You win!!")
        x+=1
    elif choice==2 and compchoice==3:
        print("You lose")
        y+=1
    elif choice==3 and compchoice==1:
        print("You lose")
        y+=1











