#write a program to append a file with the content of another file
file1=input("enter the name of first file:")#input file
file2=input("enter the name of second file:")

#open files in read mode
f1=open(file1,"r")
f2=open(file2,"r")

#print content of both file before appending
print("content of first file before apppend:",f1.read())
print("content of second file before apppend:",f2.read())

f1.close()
f2.close()

#append
f1=open(file1,"r")
data2=f1.read()
f1.close()

f2=open(file2, "a")
f2.write(data2)
f2= open(file2, "r")
data3=f2.read()
f2.close()

#print the content after append
print("content of first file after apppend:",data2)
print("content of second file after apppend:",data3)
f1.close()
f2.close()

'''output
enter the name of first file:D:\myfile.txt
enter the name of second file:D:\myfile2.txt
content of first file before apppend: hello world.
welcome to the world of python.

content of second file before apppend: hello world.
welcome to the world of python.

content of first file after apppend: hello world.
welcome to the world of python.

content of second file after apppend: hello world.
welcome to the world of python.
hello world.
welcome to the world of python.
'''
