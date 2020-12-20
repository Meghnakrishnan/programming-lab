# Take input of age of 3 people by user and determine oldest and youngest among them.

a=int(input("enter age of first person:"))#input age of first person
b=int(input("enter age of second person:"))#input age of second person
c=int(input("enter age of third person:"))#input age of third person
if(a<b and a<c):
    print("first person is youngest")
elif(b<a and b<c):
    print("second person is youngest")
elif(c<a and c<b):
    print("third person is youngest")
if(a>b and a>c):
    print("first person is oldest")
elif(b>a and b>c):
    print("second person is oldest")
elif(c>a and c>b):
    print("third person is oldest")

#output
enter age of first person:87
enter age of second person:45
enter age of third person:85
second person is youngest
first person is oldest
