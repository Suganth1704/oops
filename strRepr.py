#To return meaningful string representation we have to override __str__() method.
class Student: 
    def __init__(self,name,rollno): 
        self.name=name 
        self.rollno=rollno 

    def __str__(self): 
         return 'This is Student with Name:{} and Rollno:{}'.format(self.name,self.rollno)

s1=Student('Durga',101) 
s2=Student('Ravi',102) 
print(s1) 
print(s2) 