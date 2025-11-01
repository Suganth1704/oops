#Composition

class StudentId:

    def __init__(self,name,id,game):
        self.name=name
        self.id=id
        self.game=game

    def show(self):
        print("Name : {}\nRollNo : {}".format(self.name,self.id))

class SportsId:

    def __init__(self,obj):
        self.obj=obj
        self.student=StudentId(self.obj.name,self.obj.id,self.obj.game)
    
        
    def showi(self):
        
        print("SportsId detail\nName : {}\nrollNo : {}\nSports : {}".format(self.student.name,self.student.id,self.student.game))


if __name__=='__main__':
    s=StudentId('Suganth',44,'Basketball')
    t=SportsId(s)
    s.show()
    t.showi()
