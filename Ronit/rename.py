import os
old_file=input("Enter the Name of the file to Rename : ")
new_file=input("Enter the Name you want to give to file : ")
os.rename(old_file,new_file)