import numpy
import pandas
import os

print("File works for me")


f=open("entekhab vahed.txt","r")
print(f.read())
f.close()

b=open("entekhab vahed.txt","a")
b.write("     agha kivan")
b.close()

temp=open("entekhab vahed.txt","r")
print(temp.read())
temp.close()



os.remove("entekhab vahed.txt")