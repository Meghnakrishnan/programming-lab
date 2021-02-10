'''Create Rectangle class with attributes length and breadth and
methods to find area and perimeter. Compare two Rectangle
objects by their area using constructor'''

class rectangle():#a class named rectangle
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):#method
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)
   

length=int(input("enter the length of first rectangle:"))#enter values
breadth=int(input("enter the breadth of the first rectangle:"))

rectangle1=rectangle(length,breadth)

print("Area of first rectangle=",rectangle1.area())
print("perimeter of first rectangle=",rectangle1.perimeter())

print()
length=int(input("enter the length of second rectangle:"))
breadth=int(input("enter the breadth of second rectangle:"))

rectangle2=rectangle(length,breadth)

print("Area of first rectangle=",rectangle2.area())
print("perimeter of first rectangle=",rectangle2.perimeter())

print()

#to compare two rectangle by their area
if(rectangle1.area()>rectangle2.area()):
    print("Area of first rectangle is greater")
elif(rectangle1.area()==rectangle2.area()):
    print("Area of both rectangle are same")

else:
    print("Area of second rectangle is greater")

'''output
enter the length of first rectangle:4
enter the breadth of the first rectangle:5
Area of first rectangle= 20
perimeter of first rectangle= 18

enter the length of second rectangle:4
enter the breadth of second rectangle:5
Area of first rectangle= 20
perimeter of first rectangle= 18

Area of both rectangle are same
'''
