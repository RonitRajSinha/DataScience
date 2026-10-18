print("program started")
n1=int(input("Enter a Number:"))
n2=int(input("Enter another Number:"))
print("program ended")
try:
    n3=n1/n2
    print("The result is ",n3)

except Exception as e:
    print("Exception Occured : A number can not be divided by zero.")
print("program ended!")
