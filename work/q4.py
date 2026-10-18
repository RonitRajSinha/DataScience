'''Create a Calculator that handles:
    a.)Invalid Input
    b.)Division by Zero
    c.)Invalid Operator
'''
try:
 a1=int(input("Enter First Number : "))
 a2=int(input("Enter Second Number : "))
 op=input("Enter the operation you want to(+,-,*,/) :")

 if op=='+':
  result=a1+a2
 elif op=='-':
  result=a1-a2
 elif op=='*':
  result=a1*a2
 elif op=='/':
  if a2==0:
    raise ZeroDivisionError("Cannot divide by zero")
  result=a1/a2
 else:
  raise ValueError("Invalid Operator")

 print("Result : ",result)

except ValueError as e:
 print("Error invalid input")

except ZeroDivisionError as f:
 print("Error :",f)


