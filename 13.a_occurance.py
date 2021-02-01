#Store a list of first names. Count the occurrences of ‘a’ within the list

name=input("enter first names seperated by comma:")     #input names
a=name.split(",")   #split names by comma
print(a)            #print a list

c=name.count("a")   #count occurance of a in list 'name' and store in 'c'
print(c)            #print  value in c  

'''output
enter first names seperated by comma:athira,anu,ananya
['athira', 'anu', 'ananya']
6
'''
