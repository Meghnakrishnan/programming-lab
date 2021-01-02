#Write a Python function to sum all the numbers in a list.

n=int(input("enter number of elements in a list:"))#input number of elements in list
list=[] #initialise a list
for i in range(n): #to insert elements in list
    numbers = int(input('Enter number '))
    list.append(numbers)
def sumfun(list): #function to calculate list of numbers
    total=0
    for i in list:
        total += i
    return total    

print("Sum of elements in given list is :", sumfun(list)) #display sum

#output
enter number of elements in a list:3
Enter number 1
Enter number 2
Enter number 3
Sum of elements in given list is : 6
