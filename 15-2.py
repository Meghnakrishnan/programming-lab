''' Write a Python function to get a new string from a given string where “Is” has
been added to the front. If the given string already begins with “Is” then return
the string unchanged.'''

def string1(s):
    #check for 'Is' present already in string
    if "Is" in s:
        print(s)
    #if not then add "Is" in front of string
    else:
        print("Is "+s)

s="anu present"
string1(s)

''' output
Is anu present
'''
