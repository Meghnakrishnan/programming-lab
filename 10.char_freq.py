#Count the number of characters(character frequency) in a string.

str1=input("ente the string:")
#print and count the number of characters
for i in set(str1):
    print("number of ",i)
    print(str1.count(i))
    
'''output
ente the string:apple
number of  l
1
number of  e
1
number of  p
2
number of  a
1
'''
