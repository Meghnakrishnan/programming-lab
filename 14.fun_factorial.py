'''Write a Python function to calculate the factorial of a number (a non-negative
integer). The function accepts the number as an argument.'''

num=int(input("enter a number")) #input number
def fact(num): #function to calculate factorial
    fac = 1
    i = 1
    while i <= num:#execute loop until condition become false
        fac = fac * i#calculate factorial
        i = i + 1#i increment by 1
    return fac
print("factorial of ", num, " is ", fact(num))#display factorial

#output
enter a number4
factorial of  4  is  24
