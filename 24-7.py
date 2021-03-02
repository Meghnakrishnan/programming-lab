#8 create a class time with private attribute hour,minute and second.overload '+' operator to find sum of 2 time
class time:
    def __init__(self,h,m,s):
        self.hour=h
        self.minute=m
        self.second=s
    def __add__(self,other):
        h=self.hour + other.hour
        m=self.minute + other.minute
        s=self.second + other.second
        if(s>=60):
            m=m+1
            s=s-60
            
        if(m>=60):
            h=h+1
            m=m-60
        return h,m,s
    
print("\thour,minute,second")
tym1=time(2,40,50)
tym2=time(5,30,30)
add = tym1 + tym2

print("adding time:",add)

'''
----output----

	hour,minute,second
adding time: (8, 11, 20)
'''
