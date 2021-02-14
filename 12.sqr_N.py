#Square of N numbers
n=int(input("enter limit:")) #input a number
list=[(x*x) for x in range(1,n+1)] #compute square of numbers from 1 to limit
print(list) #print list

    
#output
enter limit:6
[1, 4, 9, 16, 25, 36]
