#write a python program to read a file line by line and store it into a list
file=input("enter the name of file:")
f=open(file,"r")
line=f.read()
lines=line.split("\n")
for line in lines:
    print(line)
f.close()

'''output
enter the name of file:D:\myfile2.txt
hello world.
welcome to the world of python.
'''