'''Write a Python program that prints all the numbers from 0 to 10 except 2 and 5.
(Use 'continue' statement.)'''

num=0,1,2,3,4,5,6,7,8,9,10
for val in num:

'''if the value is 2 or 5 then discards the remaining statements in
the current loop and goes to for loop else print the number'''
    if val==2: 
        continue
    elif val==5:
        continue
    print(val)

#output
0
1
3
4
6
7
8
9
10
