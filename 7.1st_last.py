 #Given a list of numbers, print True if first and last number of a list is same

alist=input("enter a list of numbers seperated by comma:")

if(alist[0]==alist[-1]): #check whether first and last element of list is same or not
    print("True")
else:
    print("first and last number of list is not same")


#output
enter a list of numbers seperated by comma:6,8,9,6
True
