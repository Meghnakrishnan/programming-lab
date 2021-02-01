#1.Write lambda functions to find area of square, rectangle and triangle.


p=int(input("enter the side of a square:"))
square=lambda x:x*x  #calculate area of square 
print("Area of square",square(p))

l=int(input("enter length of a rectangle:"))
b=int(input("enter breadth of a rectangle:"))
rectangle=lambda l,b:l*b #calculate area of rectangle
print("Area of recctangle:",rectangle(l,b))

x=int(input("enter base of a triangle:"))
y=int(input("enter height of a triangle:"))
triangle=lambda x,y:(x*y)/2 #calculate area of triangle
print("Area of triangle:",triangle(x,y))


''' -----output----
enter the side of a square:3
Area of square 9
enter length of a rectangle:4
enter breadth of a rectangle:5
Area of recctangle: 20
enter base of a triangle:5
enter height of a triangle:8
Area of triangle: 20.0   '''
