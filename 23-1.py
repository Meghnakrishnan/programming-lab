'''
1. Write a Python program to write a Python dictionary to a csv file. After
writing the CSV file read the CSV file and display the content.
'''

import csv
with open('employee.csv','r')as f:
    f1 = csv.DictReader(f)
    for row in f1:
        print(dict(row))

'''output
{'employeeId': '1', 'employeeName': 'ab', 'DOB': '05/11/1995/', 'salary': '11000'}
{'employeeId': '2', 'employeeName': 'cd', 'DOB': '10/5/1993', 'salary': '14000'}
{'employeeId': '3', 'employeeName': 'ef', 'DOB': '03/03/1994', 'salary': '16000'}
'''
