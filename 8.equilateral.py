'''Write a Python program to check a triangle is equilateral, isosceles or scalene.
    Note :
    An equilateral triangle is a triangle in which all three sides are equal.
     A scalene triangle is a triangle that has three unequal sides.
     An isosceles triangle is a triangle with (at least) two equal sides.'''

#to input 3 sides of a triangle
a=int(input("enter first side of triangle:"))
b=int(input("enter second side of triangle:"))
c=int(input("enter third side of triangle:"))
#to check the triangle is equilateral,isosceles or scalene
if(a==b==c):
    print("The triangle is equilateral")
elif(a==b or b==c or c==a):
    print("The triangle is isosceles")
else:
    print("The triangle is scalane")

#output
enter first side of triangle:4
enter second side of triangle:7
enter third side of triangle:7
The triangle is isosceles
