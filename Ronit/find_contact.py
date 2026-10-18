import os
name=input("Enter Your Name : ")
age=input("Enter Your Age : ")

nof=name+age+".txt"

if os.path.exists(nof):
    file=open(nof,'r')
    phone=file.readline()
    phone=file.readline()
    print(phone)
else: print("FILE NOT FOUND.")

file.close()
