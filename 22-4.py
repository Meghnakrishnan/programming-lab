#write a python program to read a file line by line and store it into a list
with open("D:\myfile2.txt")as f:    #opening file
    content_list=f.readlines()  #read line in file and store into a list
print(content_list) #print the list

'''output
['hello world.\n', 'welcome to the world of python.\n', 'hello world.\n', 'welcome to the world of python.\n']
'''
