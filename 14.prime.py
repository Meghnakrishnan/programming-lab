'''Write a Python function that takes a number as a parameter and check the
number is prime or not. '''

#input number
n=int(input("enter a number to check prime or not:"))

#check the number is prime or not.
def prime(n):
    
'''if number is 1 return 'false'
if number is 2 return 'true'
else check number is prime or not'''
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True
    
print("%s is prime:" %n,prime(n))


#output
enter a number to check prime or not:11
11 is prime: True
