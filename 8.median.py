#Write a Python program to find the median of three values

#input 3 values
a=int(input("enter first value:"))
b=int(input("enter second value:"))
c=int(input("enter third value:"))

#compare the values and print median
if(a>b):
    if(a<c):
        median=a
    elif(b>c):
        median=b
    else:
        median=c
else:
    if(a>c):
        median=a
    elif(b<c):
        median=b
    else:
        median=c
print("median is ",median)

#output
enter first value:11
enter second value:7
enter third value:64
median is  11
