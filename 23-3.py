'''3. Create a department csv file with fields- DeptId, DeptName,
Totalemployees, location. Write a Python program to read specific
columns (DeptId, DeptName) of the given CSV file and print the content
of the columns.'''

import csv
$store datas in field_list
field_list=[["DeptId","DeptName","Totalemployees","location"],
        ["1","ab","5","pmna"],
        ["2","cd","10","tkd"],
        ["3","ef","20","pkd"]]
#open department csv file in 'w' mode
with open('department.csv','w',newline='')as file:
    writer=csv.writer(file)
    writer.writerows(field_list)
with open('department.csv','r',newline='')as file:
    rows=csv.DictReader(file)
    print("department id and department")
    #to print department id and department
    for row in rows:
        print(row['DeptId'],row['DeptName'])
    
'''output
department id and department
1 ab 
2 cd
3 ef
'''
