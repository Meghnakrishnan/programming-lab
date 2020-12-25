#program to get the 3rd element and 3rd element from last of a tuple


x=input("enter some comma seperated elements :") #input elements
list=x.split(",")
y=tuple(list)
print(y) #display tuple
index=y.index
z=y[2] #third element of tuple 
print("third element of tuple is:",z)
a=y[-3] # 3rd element from last of a tuple
print("3rd element from last of a tuple is :",a)


#output
enter some comma seperated elements :3,66,8,2,9,1
('3', '66', '8', '2', '9', '1')
third element of tuple is:8
3rd element from last of a tuple is :2
