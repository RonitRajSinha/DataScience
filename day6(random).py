from random import *
num=int(input("Enter a 2-digit number : "))
n=randint(10,100)
print(n)
if num==n:
    print("Guessing Matched !!! /nYou Won :)")
elif num<n:
    print("You Guessed The Smaller value")
else : 
    print("You Guessed The Larger Value")