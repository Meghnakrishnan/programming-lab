''' Enter 2 lists of integers.
Check
(a) Whether list are of same length
(b) whether list sums to same value
(c) whether any value occur in both'''

a=list(map(int,input("enter some numbers for list1:").split()))
b=list(map(int,input("enter some numbers for list2:").split()))
print()

#if length of both list are same then print length of lists
if len(a)==len(b):  
    print("lengt of first list is:",len(a))     
    print("lengt of second list is:",len(b))    
    print("list are of same length")

#print length of lists since length are of different
else:                                               
    print("length of first list is:",len(a))
    print("length of second list is:",len(b))     
    print("list are of different length")
print()
#if sum of lists are same then print their sum
if(sum(a)==sum(b)):
    print("sum of first list is:",sum(a))
    print("sum of second list is:",sum(b))
    print("list sum to same value")
#print sum of lists if sum are of different
else:
    print("sum of first list is:",sum(a))
    print("sum of second list is:",sum(b))
    print("list sum to different value")
print(

#check whether any value occur in both and print if any
for i in a:
    for j in b:
        if i==j:
            print("%d occured in both list"%i)


'''output
enter some numbers for list1:1 5 7
enter some numbers for list2:7 5 8 9


length of first list is: 3
length of second list is: 4
list are of different length


sum of first list is: 13
sum of second list is: 29
list sum to different value


5 occured in both list
7 occured in both list
'''
    
