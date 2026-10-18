#wap to accept student marks. If marsk are outside the range 0-100 raise a ValueError
try:
    marks=int(input("Enter Your Marks : "))
    if marks<=100 and marks>=0:
        print("You obtained ",marks)
    else:
        raise Exception("Marks entered is not within the range.")

except (ValueError,Exception) as v:
    print("enter valid input")