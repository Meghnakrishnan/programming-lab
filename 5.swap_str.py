#Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.

#input strings
str1=input("enter first string:")
str2=input("enter second string:")

#perform task
new=str2[:2]+str1[2:]+' '+str1[:2]+str2[2:]

#display new string by swap the first 2 chars of each string with space 
print(new)

#output
enter first string:good
enter second string:morning
mood gorning
