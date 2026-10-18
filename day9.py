'''day 9
19/09/2026
write a program to input name of user and name of student and marks of student and print their score reports as like
----------------------------------------------------------------------
                  SCORE REPORT OF <NAME OF STUDENT>
----------------------------------------------------------------------
SID   NAME   SUB1   SUB2   SUB3   TOTAL PER   GRAD
H101  70     88      88
----------------------------------------------------------------------
   '''

student_name=input("Enter Your Name: ")
sid=input("Enter Your Id: ")
sub1=int(input("Enter Your marks of SUB1: "))
if sub1<=30:
   print("You failed")
elif sub1>100:
   print("INVALID")
   exit() 
sub2=int(input("Enter Your marks of SUB2: "))
if sub2<=30:
   print("You failed")
elif sub2>100:
   print("INVALID")
   exit()
sub3=int(input("Enter Your marks of SUB3: "))
if sub3<=30:
   print("You failed")
elif sub3>100:
   print("INVALID")
   exit()

#total marks   
total=sub1+sub2+sub3

#percentage
perc=((total/300)*100)

#GRADES
if perc>=80:
  grad="A+"
elif perc>=60:
  grad="A"
elif perc>=45:
  grad="B"
elif perc>=30:
  grad="C"
else: grad="F"

#Pass or Fail
if sub1<=30 or sub2<=30 or sub3<=30:
  status="FAIL"
else: status="PASS"
 


print('-'*50)
print(' '*10,"SCORE REPORT OF ",student_name)
print('-'*50)
print("SID   ","SUB1   ","SUB2   ","SUB3   ","TOTAL   ","%   ","GRADE   ","PASS   ")
print(sid,"   ",sub1,"   ",sub2,"    ",sub3,"   ",total,"   ",perc,"   ",grad,"   ",status,"   ")
print('-'*50)

