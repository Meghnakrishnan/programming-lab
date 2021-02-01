'''Write a function func1() such that it can accept a variable length of arguments
and return the minimum among all argument values. Print the result.'''

def func1(*args):
    for x in args:
        print(x)
func1(3,6,9)
func1(80,100)


'''output
3
6
9
80
100
'''
