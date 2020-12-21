#Find the sum of all items in a list. User should enter elements of the list.

lst = [] #initialise list
num = int(input("enter the number of elements in list:"))#input the no: of elements in list
for n in range(num): 
    numbers = int(input("Enter number ")) #read numbers in list
    lst.append(numbers) #append the given numbers to list
print("Sum of elements in given list is :", sum(lst)) #display sum of elements in list

#output
enter the number of elements in list:4
Enter number 2
Enter number 8
Enter number 6
Enter number 4
Sum of elements in given list is : 20
