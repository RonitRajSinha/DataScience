#wap that accept a number and checks whether it is positive , negative, or zero handle invalid input
try:
    num=int(input("Enter the Number : "))
    if num>0:
        print("The Entered Number is Positive.")
    elif num<0:
        print("The Entered Number is Negative.")
    else:
        print("The Entered Number is zero.")

except Exception as e:
    print("Invalid Input")