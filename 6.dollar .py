'''python program to get a string from a given string where all
occurrences of its first char have been changed to $, except the first char
itself.[ex: oniononi$n]'''


#input from user
str1=input("enter a string:")

#replacing by $
x=str1[0]+str1[1:].replace(str1[0],"$")

#display new string
print(x)


#output
enter a string:onion
oni$n
