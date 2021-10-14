'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''
import random
y=0
b=0
x=-20
print("Water, earth, fire air.")
print("Long ago, the four nations lived in harmony.")
print("But then, everything changed when the fire nation attacked")
print("Only the avatar, master of all four elements could stop him. But when the world needed him most, he vanished.")
print("100 years later, my brother and I discovered the new avatar, and air-bender named Aang")
print("And although his air-bending skills are great, he has a lot to lear before he's ready to save anyone.")
print("But I believe, Aang can save the world.")
print("Chapter 28, The Chase")
print()
print("After having Toph join the group to teach Aang earth-bending, the group plans to fly to Ba Sing Se to meet the Earth king.")
print("When the group stays the night in a forest clearing, Katara and Toph fight over Toph's responsibilties in the group.")
print("While they are arguing, Sokka notices a mysterious machine coming towards them.")
print("They decide to simply out-fly the machine, but that doesn't work so well.")
print("The machine seems to be tracking them.")
print("Meanwhile, Prince Zuko tracks the machine and his uncle Iroh travles on his own. ")
print()
print()
done=False
while done==False:
    print("Should Aang:")
    print("A.Keep flying")
    print("B.Find a place to rest")
    print("C.Fight the machine")
    print("D.Fly Faster")
    print("E.Status Check")
    print("F.Quit")
    rest_spot=random.randint(1,20)
    if rest_spot==15:
        print("Appa has found a place where Azula can't catch them. They rest, but Azula is still on the move.")
        b=0
        x+=1
    choice=str(input("What should Aang like do?"))
    if choice.lower()=="c":
        fight_now=random.randint(1,25)
        if fight_now==17:
            print("Aang has managed to defeat Azula")
            break
        else:
            print("Aang has lost against Azula. Game over")
            break
    elif choice.lower()=="a":
        print("Appa keeps flying. Azula is faster though.")
        b=b+1
        x=x+1
        y=y+1
    elif choice.lower()=="b":
        print("The group had an hours rest. Azula is getting closer")
        b=b-2
        x=x+4
    elif choice.lower()=="d":
        print("Appa has gained speed, but Appa is getting tired")
        b=b+2
        x=x-3
        y=y+2
    elif choice.lower()=="e":
        print("Azula is", x, "miles behind")
        print("Appa's tiredness is at level", b)
        print("Aang has traveled", y, "miles")
    else:
        print("You have left Aang and his friends.")
        break
    if x == 0:
        print("Azula has caught up to Aang. They have lost")
        break
    if b == 10:
        print("Appa is too tired and Azula has caught Aang.")
        break
    if y>5 and y<10:
        print("A falling out with Katara over responsiblities in the group caused Toph to go out on her own.")
        continue
    if y>14 and y<18:
        print("Aang and frieneds discovered that Appa's shedding have been letting Azula track them.")
        print("This leads Aang to split up with Sokka and Katara")
        print("Meanwhile, Toph and Iroh share a cup of tea and some friendly advice")
        print("Zuko still tracks the machine.")
        continue
    if y == 30:
        print("All parties converge at an abandoned town. It is time for the avatar and company to fight Azula.")
        done=True
        y+=1
    if y == 1:
        print("Three lizards with riders emerge from the machine. ")
        print("It is revelaed that the riders are Zuko's sister Azula, and her friends Ty Lee and Mai.")
        continue
    if b>6:
        print("Appa is getting dangerously tired.")
    if x>-6:
        print("Azula is getting very close.")
if y == 30:
    print("Aang has arrived at an abandoned Earth Kingdom town. He sits and waits as Azula speaks.")
    print("Suddenly Zuko bursts through a rooftop, aiming his fists at both Aang and Azula")
    print("Azula fires at Zuko, knocking him back, and then turns to Aang.")
while y == 31:
    for i in range(1):
        print("Aang has arrived at an abandoned Earth Kingdom town. He sits and waits as Azula speaks.")
        print("Suddenly Zuko bursts through a rooftop, aiming his fists at both Aang and Azula")
        print("Azula fires at Zuko, knocking him back, and then turns to Aang.")
    print("A. Air-bend away")
    print("B. Attack Azula")
    print("C. Help Zuko")
    fight=str(input("What should Aang do?"))
    if fight.lower()=="a":
        print("Aang escaped, but Azula is still around and kicking")
    elif fight.lower()=="b":
        print("Aang is too tired to attack")
    else:
        print("Aang helped Zuko up and they both corner Azula.")
        y+=1
if y == 32:
    print("Katara, Toph, Iroh, and Sokka arrive and help Aang and Zuko back Azula into a corner.")
    print("Azula surrenders, but then attacks Iroh and escapes.")
    print("Iroh is in critical condition")


