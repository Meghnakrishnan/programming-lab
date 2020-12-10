'''Given a two integer numbers return their product and if the product is greater
than 1000, then return their sum'''
#input 2 integers from user
a=int(input("enter first number:"))
b=int(input("enter second number:"))
#find product of that numbers
p=a*b
print("product of %s,%s:"%(a,b),p)

if(p>1000):
    sum=(a+b)
    print("sum of %s,%s:"%(a,b),sum)



#output
enter first number:69
enter second number:74
product of 69,74: 5106
sum of 69,74: 143
