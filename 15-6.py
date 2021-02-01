#write python function to generate all factors of a number
def factors(n):
    print("factors of %d are:",n)
    #checking factors of the given number
    for i in range(1,n+1):
        if (n%i==0):
            print(i)#print the factors
n=int(input("enter the number:"))#input a number
factors(n)

'''output
enter the number:20
factors of %d are: 20
1
2
4
5
10
20
'''
