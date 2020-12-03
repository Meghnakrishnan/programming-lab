
#python program to change a given string to a new string where 1st & last char have been exchanged

str1=(input("enter string:"))
new=str1[-1:] + str1[1:-1] + str1[:1]

#display string by exchanging first and last character
print("new string",new)



#0utput
enter string:black
new string klacb
