#To get days between two given dates

from datetime import date
first_date = date(2019, 7, 2)
last_date = date(2019, 7, 11)
dtes = last_date - first_date
print(dtes.days)

'''
output
9
'''
