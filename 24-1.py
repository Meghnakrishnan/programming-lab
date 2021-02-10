'''Exercise 24

1. Create Rectangle class with attributes length and breadth and
methods to find area and perimeter. Compare two Rectangle
objects by their area.'''

class rectangle():#a class named rectangle
    def lenbre(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):#method
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)
   
obj1=rectangle()#object created
length=int(input("enter the length of first rectangle:"))#enter values
breadth=int(input("enter the breadth of the first rectangle:"))

obj1.lenbre(length,breadth)

print("Area of first rectangle=",obj1.area())
print("perimeter of first rectangle=",obj1.perimeter())

obj2=rectangle()
print()
length=int(input("enter the length of second rectangle:"))
breadth=int(input("enter the breadth of second rectangle:"))

obj2.lenbre(length,breadth)

print("Area of first rectangle=",obj2.area())
print("perimeter of first rectangle=",obj2.perimeter())

print()

#to compare two rectangle by their area
if(obj1.area()>obj2.area()):
    print("Area of first rectangle is greater")
elif(obj1.area()==obj2.area()):
    print("Area of both rectangle are same")

else:
    print("Area of second rectangle is greater")


'''output
enter the length of first rectangle:10
enter the breadth of the first rectangle:20
Area of first rectangle= 200
perimeter of first rectangle= 60

enter the length of second rectangle:25
enter the breadth of second rectangle:15
Area of first rectangle= 375
perimeter of first rectangle= 80

Area of second rectangle is greater
'''
