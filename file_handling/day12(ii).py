#write a program to input name of customer,phone, product, quantity, price and generate bill with gst of each cutomer with their name+phone.
customer=input("Enter Your Name : ")
phone=int(input("Enter Phone Name : "))
product=input("Enter Product Name : ")
price=int(input("Enter price : "))
qnt=int(input("Enter qnt : "))

subtotal=price*qnt
gst=subtotal*18/100
total=subtotal+gst

d=[customer,phone,product,price,qnt,subtotal,gst,total]
bill=str(d)



file=customer+".txt"
data=open(file,'w')
data.writelines("Customer  phone  product  price  qnt  subtotal  gst  total")
data.writelines(d)

