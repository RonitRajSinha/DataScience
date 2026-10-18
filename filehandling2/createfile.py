import os
nof=input("ENTER THE NAME OF FILE : ")

if os.path.exists(nof):
    fn=input("File already exists enter another file : ")
    file=open(fn,'w')

else: file=open(nof,'w')