''' Write a python function to calculate the simple interest. (Use Keyword
Arguments)'''

def simple_interest(amnt,time,rate):
    #finding simple interest
    si=amnt*time*(rate/100)
    return si
#enter inputs
p=int(input("enter the principle amount:"))
t=int(input("enter the no: years:"))
r=int(input("enter the rate of interest:"))
#function call
x=simple_interest(amnt=p,rate=r,time=t)
#print simple interest
print("simple interest=",x)
      
    
'''output
enter the principle amount:10000
enter the no: years:3
enter the rate of interest:2
simple interest= 600.0
'''
