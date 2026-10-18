#write a program to input name and age of a person and print he or she is eligible for vote

name=input("enter your name : ")
age=int(input("enter your age : "))

if (age>=18):
        print(name," is eligible to vote.")
else:
        print(name," is not eligible to vote.")
