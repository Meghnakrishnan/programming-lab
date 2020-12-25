#write a python program to remove an item from a tuple
m=input("how many item in tuple:") #input number of elements
x=input("enter %s comma seperated elements:"%m) #input elements
list=x.split(",")
tuple1=tuple(list)
print(tuple1) #print a tuple
item=input("enter an item to remove:") #input item to remove
index=tuple1.index(item) #find index of given item
tuple2=tuple1[0:index]+tuple1[index+1:] #removal process
print("after removal of %item:",tuple2) #display tuple after removal of specified item


#output
how many item in tuple:3
enter 3 comma seperated elements:21,6,9
('21', '6', '9')
enter an item to remove:21
after removal of %item: ('6', '9')
