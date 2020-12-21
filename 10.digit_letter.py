'''Write a Python program that accepts a string and calculate the number of digits
and letters.(isdigit(), isalpha())'''

str1=input("enter a string:")#input string
d=a=0
for val in str1:
    if val.isdigit(): #check whether val is number or not
        d=d+1 #count the number of digits
    elif val.isalpha(): #check whether val is alphabet or not
        a=a+1 #count the number of alphabets
    else:
        pass
print("number of digits in %s is:" %(str1),d) #displa number of digits in given string
print("number of letters in %s is:" %(str1),a) #display number of letters in string

#output
enter a string:hello13
number of digits in hello13 is: 2
number of letters in hello13 is: 5
