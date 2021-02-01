#write a program to append a file with the content of another file
file1=input("enter the name of first file:")
file2=input("enter the name of second file:")

f1=open(file1,"r")
f2=open(file2,"r")

print("content of first file before apppend:",f1.read())
print("content of second file before apppend:",f2.read())

f1.close()
f2.close()

f1=open(file1,"r")
data2=f1.read()
f1.close()
f2=open(name2, "a")
f2.write(data2)
f2= open(name2, "r")
data3=f2.read()
f2.close()

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
'''
