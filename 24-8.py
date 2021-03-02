#Write a Program to implement the following. 
#Create a base class called Person consisting of name and code. Create 2  child classes 
#A) Account with member pay 
#B)Admin with experience 
#Create a class Employee with name, code, experience and pay by  inheriting the above classes.


class Person():
    def __init__(self,name,code):
        self.name=name
        self.code=code
      
    def DisplayPerson(self):
        print("Name : ",self.name)
        print("Code : ",self.code)  
        
class Account(Person):
    def __init__(self,pay):
        self.pay=pay
        
    def DisplayAccount(self):
        print("Payment : ",self.pay)
        
class Admin(Person):
    def __init__(self,experience):
        self.experience=experience
        
    def DisplayAdmin(self):
        print("Experience : ",self.experience)  
        
        
class Employee(Account,Admin):
    def __init__(self,name,code,pay,experience):
        Person.__init__(self,name,code)
        Account.__init__(self,pay)
        Admin.__init__(self,experience)
        
obj=Employee("meenu","123","4000","3")

obj.DisplayPerson()
obj.DisplayAccount()
obj.DisplayAdmin()
        
'''
Name :  meenu
Code :  123
Payment :  4000
Experience :  3
'''
