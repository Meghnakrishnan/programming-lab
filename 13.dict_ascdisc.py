#Sort dictionary in ascending and descending order.

dict1={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}#dictionary in dict1
dict2=list(dict1.items()) #convert to list
dict2.sort() #sort in ascending order
print('Ascending order is',dict2) #print dictionary in ascending order
dict2.sort(reverse=True) #sort in descending order
print('Descending order is',dict2) #print dictionary in descending order

#output
Ascending order is [(0, 0), (1, 2), (2, 1), (3, 4), (4, 3)]
Descending order is [(4, 3), (3, 4), (2, 1), (1, 2), (0, 0)]
