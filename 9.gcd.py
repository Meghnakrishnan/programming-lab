#Find the greatest common divisor (GCD) of two integers

#input 2 integer
a=int(input("enter first integer:"))
b=int(input("enter sec0nd integer:"))

while b!=0:
    temp=b
    b=a%b
    a=temp
gcd=a
print("gcd is:",gcd)#print gcd


#output
enter first integer:200
enter sec0nd integer:240
gcd is: 40
