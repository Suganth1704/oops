class Duck:
    def talk(self):
        print("I am duck")

class Dog:
    def bark(self):
        print("I am dog")


if __name__=='__main__':
    def f(obj):
        if hasattr(obj,'talk'):
            return obj.talk()
        else:
            return obj.bark()
        
    ob=Dog()
    ob1=Duck()
    f(ob)
    f(ob1)