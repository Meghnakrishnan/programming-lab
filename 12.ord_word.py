#List ordinal value of each element of a word (Hint: use ord() to get ordinal values)

str="hello" #a string
ord1=[ord(x) for x in str] #find ordinal value of each element in string
print(ord1) #print ordinal value of string as list

#output
[104, 101, 108, 108, 111]
