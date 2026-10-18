name=input("Enter Your name :")
roll_no=int(input("Enter Your Roll Code: "))
total=0
for i in range(5):
   subject_name=input("Enter The Subject Name: ")
   subject_marks=int(input(f"Enter The {subject_name} Marks: "))
   if subject_marks<30:
     print("failed")
   else: total=total + subject_marks
   
percentage=total/500*00
print("You got ",total,"out of 500")
print("You got ",total/500*100,"%")

if percentage>=90 and percentage<=100 :
     print("Grade A+")
elif percentage>=60 and percentage<=90 :
     print("Grade A")
elif percentage>=45 and percentage<=60 :
     print("Grade C")
elif percentage>=33 and percentage<=45 :
    print("Grade D")
else: print("Failed")
