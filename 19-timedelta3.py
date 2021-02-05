#To print next 5 days starting from today

import datetime  
today=datetime.date.today()  
for x in range(0, 5):  
      print(today + datetime.timedelta(days=x)) 

''' output

2021-01-19
2021-01-20
2021-01-21
2021-01-22
2021-01-23

'''
