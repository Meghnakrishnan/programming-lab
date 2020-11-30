#program to find the biggest of three numbers using max()

def maximum(a,b,c):
 list=[a,b,c]
 return max(list)
#input numbers
p=int(input("enter first number:"))
q=int(input("enter second number:"))
r=int(input("enter third number:"))
#print biggest number
print("The biggest number among %s,%s,%s is: "%(p,q,r),maximum(p,q,r))

#output
enter first number:28
enter second number:3
enter third number:37
The biggest number among 28,3,37 is:  37
