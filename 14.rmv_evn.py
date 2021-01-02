#From a list of integers, create a list removing even numbers.

n=int(input("enter the numbrs of elements in a list"))
list=[]
odd=[]
for i in range(n): #to create a list
    number=int(input("enter the number"))
    list.append(number)
def oddlst(odd): #function to remove even numbers
    for x in list:
        if(x % 2!=0):
            odd.append(x)
        else:
            pass
    return odd
print(oddlst(odd))
    

#output
enter the numbrs of elements in a list6
enter the number2
enter the number4
enter the number1
enter the number3
enter the number7
enter the number9
[1, 3, 7, 9]
    
    
    
