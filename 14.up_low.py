'''Write a Python function that accepts a string and calculate the number of upper
case letters and lower case letters.'''

s=input("enter a string")# input string
def uplow(s): # function to calculate number of uppercase and lowercase 
    u=0
    l=0
    for i in s:
        if i.isupper():# check the letter is uppercase or not
            u=u+1 #count
             
        elif i.islower(): # check the letter is lowercase or not
            l=l+1
               
        else:
            pass #do nothing
    return u,l 
print("Number of upper case an lower case in the given string is",uplow(s)) #print number of uppercase and lowercase 

#output
enter a stringAppLe
Number of upper case an lower case in the given string is (2, 3)
