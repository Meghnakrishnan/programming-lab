#program to find the biggest of three numbers using max()
 
#input numbers
p=int(input("enter first number:"))
q=int(input("enter second number:"))
r=int(input("enter third number:"))
b=max(p,q,r)
#print biggest number
print("The biggest number among %s,%s,%s is: "%(p,q,r),b)

#output
enter first number:70
enter second number:95
enter third number:20
The biggest number among 70,95,20 is:  95
