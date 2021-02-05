#Display future leap years from current year to a final year entered by user.

y=int(input("enter future year:")) #input an year
if y%4==0: #check for leap year 
    print("%d is a leap year"%y) #print year is leap year
else:
    print("%d is not a leap year"%y) #print year is not leap year

#output
enter future year:2028
2028 is a leap year
