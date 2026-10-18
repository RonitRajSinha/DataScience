from random import *
students=["Vishal","Sarthak","Ankit","Sujeet","Sanu","Abhi","Arya","Ronit","Prince","Ashu","Chaya"]
ss=choice(students)
print("Enter Name Of Student from the list to win ",students," : ",end=" ")
nos=input()
print("System Selected The Student : ",ss)
if ss==nos:
    print("YOU WON THE GAME !")
else:
    print("YOU LOOSE :( ")