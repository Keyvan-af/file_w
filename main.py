import numpy
import pandas
import os


f=open("entekhab vahed.txt","r")
print(f.read())
f.close()

b=open("entekhab vahed.txt","a")
b.write("     agha kivan")
b.close()

t=open("entekhab vahed.txt","r")
print(t.read())
t.close()



os.remove("entekhab vahed.txt")