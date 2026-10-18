#wap to creating a new file with specific name and extension. 
file_name=input("Enter the name you want to give to file : ") #jan
ext=input("Enter the desirable extension of the file : ")   #txt
file_name_ext= file_name+"."+ext    #jan.txt
file=open(file_name_ext,"w")
file.write("Creating a file using the concept of file handling in python!")
file.close()