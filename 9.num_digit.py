#Given a number count the total number of digits in a number
num=int(input("enter a number"))#input a number
i=0
while num>0:
    i=i+1
    num=num//10
print("number of digitis",i)#display the number of digits
    
#output
 ===========
enter a number976
number of digitis 3
