#Write a loop to find the factorial of any number entered by user
num = int(input("enter a number: "))#input a number
fac = 1
i = 1
while i <= num:#execute loop until condition become false
    fac = fac * i#calculate factorial
    i = i + 1#i increment by 1
print("factorial of ", num, " is ", fac)#display factorial

#output

enter a number: 6
factorial of  6  is  720
