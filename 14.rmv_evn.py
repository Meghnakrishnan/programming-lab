#From a list of integers, create a list removing even numbers.

n=list(map(int,input("enter numbers seperated by commma:").split(",")))
for i in n:
    if(i % 2==0):#check for even number
        n.remove(i)
print("list after removal of even numbers:",n)

'''output
enter numbers seperated by commma:6,1,8,7
list after removal of even numbers: [1, 7]
''' 
    
    
