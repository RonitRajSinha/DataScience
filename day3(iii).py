#write a program to create a mini calculator
n1=int(input("enter first number : "))
n2=int(input("enter second number : "))
op=input("enter operator sign : ")

if(op=='+'):
    print("Sum of ", n1, "and", n2, "is",n1+n2)
elif(op=='-'):
    print("Difference of ", n1, "and", n2, "is",n1-n2)
elif(op=='*'):
    print("Product of ", n1, "and", n2, "is",n1*n2)
elif(op=='//'):
    print("Rounded of QUOTIENT of ", n1, "and", n2, "is",n1//n2)
elif(op=='/'):
    print("Quotient of", n1, "and", n2, "is",n1/n2)


