''' Write a function calculate() such that it can accept two variables and calculate
the addition, subtraction, division and Multiplication of it. And also it must
return all values in a single return call and display the results.'''

def calculate(a,b):#function definition
    sum=a+b#calculate sum
    sub=a-b#subtraction
    div=a/b#division
    mul=a*b#multiplication
    return sum,sub,div,mul
x=int(input("enter first number:"))
y=int(input("enter second number:"))
a,s,d,m=calculate(x,y)#function call
print("%d+%d=%d"%(x,y,a))
print("%d-%d=%d"%(x,y,s))
print("%d/%d=%d"%(x,y,d))
print("%d*%d=%d"%(x,y,m))

'''output
enter first number:20
enter second number:10
20+10=30
20-10=10
20/10=2
20*10=200
'''
