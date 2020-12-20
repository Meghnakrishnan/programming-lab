'''A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
     Ask user for their salary and year of service and print the net bonus amount.'''

sal=int(input("enter the salary:"))#input salary
year=int(input("enter year of service:"))#input years of service
net_bonus=(sal*5)/100#calculate net bonus amount of 5%
t=sal+net_bonus#total salary after net bonus

#execute if statement until condition become false
if(sal>5):
    print("net bonus amount:",net_bonus)#display net bonus
    print("total salary:",t)#display total salary
#execute else statement while if condition become false    
else:
    print("No bonus amount")#display no bonus amount
    print("total salary:",sal)#display total salary
        
#output
enter the salary:6000
enter year of service:7
net bonus amount: 300.0
total salary: 6300.0
