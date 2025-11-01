class Student:

    '''Student class to get student details'''

    #Constructor
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno #instance variables

    #Methods
    def show(self):
        self.school='Maria Rafols' #Instance variables in side method
        print("{}--{}--{}".format(self.name,self.rollno,self.school))
    @classmethod
    def clasMethod(cls,name):
        cls.broll=5
        print("Broll from cls method : {} Name :{}".format(cls.broll,name))

if __name__=='__main__':

    obj=Student('Suganth',44)
    print(obj.__doc__)
    print(obj.__dict__)
    obj.show()
    print(obj.__dict__)
    obj.d=44 # Instance variable declaried out side class.
    print(obj.__dict__)

    #Class Method
    Student.clasMethod('Boot')
    


        