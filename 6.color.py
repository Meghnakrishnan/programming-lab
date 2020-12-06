#Create a list of colors from comma-separated color names entered by user.Display first and last colors.

#input from user
color=input("Enter colors seperated by comma:")

list=color.split(",")
a=list[0]
b=list[-1]

#display first and last colors
print("%s is first color in the list" %a)
print("%s is last color in the list" %b)

#output

Enter colors seperated by comma:red,pink,green,black
red is first color in the list
black is last color in the list
