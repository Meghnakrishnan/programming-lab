#Write a Python program to convert month name to a number of days

month=input("enter the month:")#input month
#check mont and print corresponding no: of days
if(month=="january"):
   print("31 days")
elif(month=="february"):
   print("28 or 29 days")
elif(month=="march"):
   print("31 days")
elif(month=="april"):
   print("30 days")
elif(month=="may"):
   print("31 days")
elif(month=="june"):
   print("30 days")
elif(month=="july"):
   print("31 days")
elif(month=="august"):
   print("31 days")
elif(month=="september"):
   print("30 days")
elif(month=="october"):
   print("31 days")
elif(month=="november"):
   print("30 days")
elif(month=="december"):
   print("31 days")
else:
   print("invalid")

#output
enter the month:april
30 days
