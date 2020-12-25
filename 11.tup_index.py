#Write a Python program to find the index of an item of a tuple

values=input("enter items to tuple:")
item=input("enter an item:")
tuple1=tuple(values)
print(tuple1)
index=tuple1.index(item)
print(index)

#output
enter items to tuple:hello world
enter an item:w
('h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd')
6
