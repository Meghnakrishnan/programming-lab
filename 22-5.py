#python program to find longest word
file=input("enter the name of file:")
f=open(file,"r")
line=f.read()
words=line.split()
length=len(words)
l=words[0]
for i in range(1,length):
    if(len(words[i])>len(l)):
        l=words[i]
print("longest word:",l)
    
'''output
enter the name of file:D:\myfile.txt
longest word: welcome
'''
