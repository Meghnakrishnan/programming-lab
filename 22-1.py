#write a program to copy a text file to another file

file1=input("enter the source file to be copied:")
file2=input("enter the destination file name:")
fr=open(file1,"r")
fw=open(file2,"w")
for line in fr.readlines():
    fw.write(line)
fr.close()
fw.close()
print("file copied")

'''output
enter the source file to be copied:D:\myfile2.txt
enter the destination file name:D:\myfile12.txt
file copied
'''
