'''A student will not be allowed to sit in exam if his/her attendance is less than 75%.
Take following input from user
Number of classes held
Number of classes attended.
And print percentage of class attended and if the student is allowed to sit in exam
or not.'''

print("A student will not be allowed to sit in exam if his/her attendance is less than 75%")
a=int(input("Number of classes held:"))
b=int(input("Number of classes attended:"))
p=(b/a)*100
if(p<75):
    print("percentage of class attended is %s.You are not allowed to sit in exam"%p)
elif(p>=75):
    print("percentage of class attended is %s.You are allowed to sit in exam"%p)



#output

A student will not be allowed to sit in exam if his/her attendance is less than 75%
Number of classes held:20
Number of classes attended:15
percentage of class attended is 75.0.You are allowed to sit in exam
