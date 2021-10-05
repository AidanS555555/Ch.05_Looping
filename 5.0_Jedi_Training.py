  #Sign your name:________________

'''
 1. Make the following program work.
   '''  
print("This program takes three numbers and returns the sum.")

import random
for i in range(3):
    x = float(input("Enter a number: "))
total=x
print("The total is:",total)



'''
  2. Write a Python program that will use a FOR loop to print the even
     numbers from 2 to 100, inclusive.
'''





'''
  3. Write a program that will use a WHILE loop to count from
     10 down to, and including, 0. Then print the words Blast off! Remember, use
     a WHILE loop, don't use a FOR loop.
'''
x=10
while x>=0:
    print(x)
    x-=1
if x==0:
    print("Blast off!!!")




'''
  4. Write a program that prints a random integer from 1 to 10 (inclusive).
'''
x=random.randint(1,10)
print(x)





'''
  5. Write a Python program that will:
     
     * Ask the user for seven numbers
     * Print the total sum of the numbers
     * Print the count of the positive entries, the count of entries equal to zero,
     and the count of negative entries. Use an if, elif, else chain, not just three
     if statements.
      
'''
