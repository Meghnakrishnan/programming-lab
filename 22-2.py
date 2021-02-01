#Write a program to count the number of lines in a file.
file=open("D:\myfile2.txt","r")
count=0
rl=file.readlines()
for line in rl:
    count=count+1
print("Number of lines:",count)
file.close()

'''OUTPUT
Number of lines: 2
'''
