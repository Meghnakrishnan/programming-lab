'''Write a Python function to calculate the sum of three given numbers, if the
values are equal then return thrice their sum.'''

def sum_thrice(a, b, c): #sum_thrice function with argument a,b,c
    sum = a + b + c      #add a,b,c and store in sum
    if a == b == c:      #if a,b,c are same value then find thrice of their sum
        sum = sum * 3
    return sum
print("sum is:",sum_thrice(2, 3, 5))
print("Thrice of their sum :",sum_thrice(2, 2, 2))

'''output
sum is: 10
Thrice of their sum : 18'''
