#file handling
user_id=input("Enter your user id : ")
password=input("Enter your password : ")
file=open("password.txt","r")
uid=file.readline().strip()
pas=file.readline().strip()
if user_id==uid and password==pas:
    print("login succesfully")
elif user_id != uid and password==pas:
    print("Login Failed !\n Invalid User ID")
elif user_id==uid and password!=pas:
    print("Login Failed !\n Invalid Password")
else: print("Login Failed !\n Both Credentials Wrong")
