#Write a Python program to reverse a tuple.


values = input("Input some comma seprated numbers : ")#input numbers
list = values.split(",")
tuple = tuple(values)
y = tuple[::-1]#reverse task
print(y)#print reversed tuple

#output
Input some comma seprated numbers : 9,6,8,2,5
('5', '2', '8', '6', '9')
