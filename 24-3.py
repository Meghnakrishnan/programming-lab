'''Excercise-24

Define a class Student. Include the following details
like roll no, name and class. Write methods to assign
initial values and display student details'''

class student: #class named student
    def __init__(self,n,r,c): #constructor is defined
        
        self.name=n;
        self.rollno=r;
        self.Class=c;
    def display(self): #a method to display
        print("Name :",self.name)
        print("Rollno :",self.rollno)
        print("Class :",self.Class)

stud1=student("Meera","1","MCA S1")
stud1.display()
print()
stud2=student("Manu","2","MCA S1")
stud2.display()

         
'''output
Name : Meera
Rollno : 1
Class : MCA S1

Name : Manu
Rollno : 2
Class : MCA S1
'''
