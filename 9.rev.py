#Reverse a given integer number
num=int(input("enter an integer:"))#input an integer
rev=0#store 0 in rev
while num>0:#execute loop until condition become false
    x=num%10#remainder store in x
    rev=(rev*10)+x
    num=num//10
print("reverse is",rev)#print reverse of given number

#output
enter an integer:975
reverse is 579
