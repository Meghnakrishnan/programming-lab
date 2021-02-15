'''
2. Write a Python program to read each row from a given csv file and print
a list of strings.
'''
import csv
with open('employee.csv','r') as f:
    reader=csv.reader(f)
    for row in reader:
        print(row)

'''output
['employeeId', 'employeeName', 'DOB', 'salary']
['1', 'ab', '05/11/1995/', '11000']
['2', 'cd', '10/5/1993', '14000']
['3', 'ef', '03/03/1994', '16000']
'''
