#Print the multiplication table of a number

#input a number to compute its multiplication table
num=int(input("enter a number:"))
print("Multiplication table of",num)
i=1
while i<11:#execute while loop until the condition become false
    mul=i*num#multiplication process
    print("%s*%s=%s"%(i,num,mul))#display multiplication of number
    i=i+1#i increment by 1


#output
enter a number:3
Multiplication table of 3
1*3=3
2*3=6
3*3=9
4*3=12
5*3=15
6*3=18
7*3=21
8*3=24
9*3=27
10*3=30
