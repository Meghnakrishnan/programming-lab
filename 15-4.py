#Write a Python function to generate all the factors of a number.

def factor(n):
    print("Factors of %s are:" %n)
    for i in range(1,n+1):
        #check remainder is 0 if true then print
        if n%i==0:
            print(i)

n=20
factor(n)

'''output
Factors of 20 are:
1
2
4
5
10
20'''
