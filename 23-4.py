#4. Python program to copy odd lines of one file to other

file=input("enter a file:")
f=open(file,'r')    #open file in read mode
w=open("D:\odds.txt","w")   #open file in w mode
lines=f.readlines()
#to get odd lines
for i in range(1,len(lines)+1):
    if(i%2!=0):
        w.write(lines[i-1])

f.close()
w.close()

w=open("D:\odds.txt","r")
content=w.read()
print(content)

w.close()


'''output
enter a file:D:\oddfile.txt
line 1 
 line 3 
 line 5
 line 7
 '''
