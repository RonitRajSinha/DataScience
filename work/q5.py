#wap with nested try except blocks
try:
 n=int(input("Enter a number : "))
 try:
    if n>0:
     print("number positive")
    else:
      raise ValueError("Not positive")
 except Exception as e:
    print(e)
except ValueError as v:
  print("Invalid Input")
  