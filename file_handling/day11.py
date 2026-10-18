#wap to to input user id and password and check if userid and password match then print message login successful
user_id=(input("ENTER YOUR USER ID : "))
password=input("ENTER YOUR PASSWORD : ")
if user_id=="sinharonittt" and password=="Ronit@28":
      print("Correct Credentials\n WELCOME!",user_id)
elif user_id=="sinharonittt" and password!="Ronit@28":
      print("Wrong password !")
elif user_id!="sinharonittt" and password=="Ronit@28":
      print("wrong username")
else: print("ONE OF THE CREDENTIALS IS WRONG")
      