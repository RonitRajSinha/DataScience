#WAP TO CREATE A BILL GENERATOR
from playsound3 import *
print("-------------------------------------------")
print("Welcome to to Khatu King Tea Stall")
print("-------------------------------------------")
print("Press  1 for coffee \n Press 2  for tea \n Press 3 for cold coffee \n")
playsound("C:\\users\\ronit\\OneDrive\\Desktop\\sounds_python\\dragon-studio-cute-doorbell-chime-472376.mp3")
ch=int(input("Enter your choice : "))
if ch==1:
    print("press 1 for small \npress 2 for medium \npress 3 for large")
    chh=int(input("Enter your  choice : "))
    noc=int(input("Enter  the number :"))
    if chh==1:
          total=noc*15
    elif chh==2:
          total=noc*20
    elif chh==3:
          total=noc*25
    else:
          exit(1)
    print("Your total bill is :",total)

elif ch==2:
    print("press 1 for small \npress 2 for medium \npress 3 for large")
    chh=int(input("Enter your  choice : "))
    noc=int(input("Enter  the number :"))
    if chh==1:
          total=noc*10
    elif chh==2:
          total=noc*15
    elif chh==3:
          total=noc*20
    else:
          exit(1)
    print("Your total bill is :",total)

elif ch==3:
    print("press 1 for small \npress 2 for medium \npress 3 for large")
    chh=int(input("Enter your  choice : "))
    noc=int(input("Enter  the number :"))
    if chh==1:
          total=noc*30
    elif chh==2:
          total=noc*35
    elif chh==3:
          total=noc*40
    else:
          exit(1)
    print("Your total bill is :",total)
else:
    exit(1)

