'''program to Input a number and check if the number is positive or negative or zero and display an appropriate message'''

num = float(input("Enter a number: "))
if (num > 0):
    print("Positive number")
elif (num == 0):
    print("Zero")
else:
    print("Negative number")


#Output
Enter a number: -2
Negative number
