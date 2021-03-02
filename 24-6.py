#7 create a class rectangle with private attribute length and width.overload '<' operator to compare the area of 2 rectangles
class rectangle:
    def __init__(self, h, w):
        self.height = h
        self.width = w
    def __lt__(self, other):
        tr1=self.height * self.width
        tr2=other.height * other.width
        if tr1<tr2:
            return "area of first rectangle is less than the area of second rectangle"
        else:
            return "area of first rectangle is greater than the area of second retangle"
rectangle1=rectangle(3,4)
rectangle2=rectangle(4,5)
area=rectangle1<rectangle2
print(area)

'''output

area of first rectangle is less than the area of second rectangle
'''
