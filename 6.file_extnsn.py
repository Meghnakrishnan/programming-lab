#python program to accept a filename from the user, print extension of that

a=input("enter a filename:")
b=a.split(".")
ext=b[-1]
print("extension of filename is",ext)


#output
enter a filename:area.py
extension of filename is py
