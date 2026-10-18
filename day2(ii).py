#write a program to input name, quantity and price of a product and generate a bill with 18 percent GST
product_name=input("Enter product name: ")
quantity=int(input("Enter the Quantity: "))
price=int(input("Enter the Price: "))
Total=quantity*price
GST=Total*18//100

print("BILLING DETAILS")
print("item name-",product_name)
print("Quantity-",quantity)
print("Total Price-",Total)
print("GST@18%-",GST)
print("PRICE@18% GST INCLUDED: ", Total+GST)      
