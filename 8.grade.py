''' A school has following rules for grading system:
    a. Below 25 - F
    b. 25 to 45 - E
    c. 45 to 50 - D
    d. 50 to 60 - C
    e. 60 to 80 - B
    f. Above 80 - A
    Ask user to enter marks and print the corresponding grade.'''

mark=int(input("enter mark:"))#input mark
if mark<25:
    print("F")#display F if mark is below 25
elif mark>=25 and mark<45:
    print("E")#display E if mark is below 45 or greater than equal to 25
elif mark>=45 and mark<50:
    print("D")
elif mark>=50 and mark<60:
    print("C")
elif mark>=60 and mark<80:
    print("B")
else:
    print("A")

#output
enter mark:80
A
