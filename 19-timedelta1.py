#To Subtract five days from current date.

from datetime import date, timedelta
dt = date.today() - timedelta(5)
print('Current Date :',date.today())#print current date
print('5 days before Current Date :',dt)


#output
Current Date : 2021-01-19
5 days before Current Date : 2021-01-14
