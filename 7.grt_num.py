#Take two integer values from user and print greatest among them

#input 2 integers from use
a=int(input("enter first number"))
b=int(input("enter second number"))

#check the greatest number
if(a>b):
#display fist number if it is greatest
    print("Greatest number among %s,%s is:" %(a,b),a)
else:
#display second number 
    print("Gretest number among %s,%s is:"%(a,b),b)


#output
enter first number8
enter second number30
Gretest number among 8,30 is: 30
