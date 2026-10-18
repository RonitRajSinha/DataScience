#copy the image using this app
si=open("test.jpg",'rb')
data=si.read()
ti=open("Hubnet.jpg",'wb')
ti.write(data)
ti.close()
si.close()