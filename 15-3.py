#Write a Python function to find the sum of digits of a number.

def sumofdigit(n):
    sum=0
    for i in str(n):
        sum+=int(i)
    return sum
n=253
print("sum of digits of %s is" %n,sumofdigit(n))

''' output
sum of digits of 253 is 10
'''
