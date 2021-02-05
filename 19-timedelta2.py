#To print yesterday, today and tomorrow

import datetime 
today=datetime.date.today()
yesterday=today-datetime.timedelta(days=1)
tomorrow=today+datetime.timedelta(days=1) 
print("Yesterday :",yesterday)
print("Today :",today)
print("Tomorrow :",tomorrow)

'''output
Yesterday : 2021-01-18
Today : 2021-01-19
Tomorrow : 2021-01-20
'''
