'''Write a function func1() such that it can accept a variable length of arguments
and return the minimum among all argument values. Print the result.'''

def func1(*args):
        a=min(args)#minimum of args is stored in 'a'
        print(a)#print minimum among given value
func1(3,6,9,0,-4)#function call



'''output
-4
'''
