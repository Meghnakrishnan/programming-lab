''' A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
    Ask user for quantity
    Suppose, one unit will cost 100.
    Judge and print total cost for user.'''

q=int(input("enter the quantity to purchase:"))#input quatity 
t=(q*100)
d=((t*10)/100) 
dis=t-d #calculate cost after discount 
print("total cost:",t) #display total cost
if (t>=1000):
    print("total cost after discount:",dis) #if total cost is >= 1000 display total cost after discount
else:
    print("no discount",t) #display total cost 

#output
enter the quantity to purchase:12
total cost: 1200
total cost after discount: 1080.0
