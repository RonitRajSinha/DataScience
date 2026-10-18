'''
create a file
open file
read data from file
write data over a file 
append data over a file
copy the file/backup the file
delete the file 
rename the file 
check the properties of the file
'''
print("CONTACT BOOK")
name=input("Enter Your Name : ")
ph=(input("Enter Your PHONE NO. : "))
age=(input("Enter Your age : "))
city=input("Enter your city : ")

data=name+city+age+".txt"

c=open(data,'w')
c.writelines("Name : ",name)
c.write("Phone Number : ",ph)
c.write("")