#Prompt the user for a list of integers. For all values greater than 100, store ‘over’ instead

n=int(input("how many numbers:"))
list=[]#initialize list
for i in range(n):#to add elements to list
    num=int(input("enter number:"))
    if num>100:
        a="over"
        list.append(a)#if number>100 'over' add to list instead of number
        else:
        list.append(num)# number add to list
print(list) #display new list
     
#output
how many numbers:4
enter number:6
enter number:600
enter number:450
enter number:8
[6, 'over', 'over', 8]
