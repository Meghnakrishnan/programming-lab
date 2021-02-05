'''Exercise 24

1. Create Rectangle class with attributes length and breadth and
methods to find area and perimeter. Compare two Rectangle
objects by their area.'''

class rectangle():#a class named rectangle
    def lenbre(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):#method
        return length*breadth
    def perimeter(self):
        return 2*(length+breadth)
   
obj1=rectangle()#instance
length=int(input("enter the length or rectangle:"))#enter values
breadth=int(input("enter the breadth of the rectangle:"))
obj1.lenbre(length,breadth)
print("Area of first rectangle=",obj1.area())
print("perimeter of first rectangle=",obj1.perimeter())
a1=obj1.area()
print()
length1=int(input("enter the length of second rectangle:"))
breadth1=int(input("enter the breadth of second rectangle:"))
obj1.lenbre(length1,breadth1)
print("Area of first rectangle=",obj1.area())
print("perimeter of first rectangle=",obj1.perimeter())
a2=obj1.area()

print()

#to compare two rectangle by their area
if(a1>a2):
    print("Area of first rectangle is greater")
elif(a1==a2):
    print("Area of both rectangle are same")

else:
    print("Area of second rectangle is greater")


'''output
enter the length or rectangle:4
enter the breadth of the rectangle:2
Area of first rectangle= 8
perimeter of first rectangle= 12

enter the length of second rectangle:6
enter the breadth of second rectangle:3
Area of first rectangle= 8
perimeter of first rectangle= 12

Area of both rectangle are same
'''
