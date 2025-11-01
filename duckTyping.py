"""
Duck typing is a concept related to dynamic typing 
where the type of the class of an object is less important than the 
method it defines. Using Duck Typing we do not check types at all.
Insted we check for the presence of the given method or attribute.

 """

class Duck:
    def sound(self):
        print('quack quack')
class Dog:
    def sound(self):
        print('woof woof')
class Cat:
    #1 def sound(self):
    #     print('meow meow')

    def __init__(self):
        self.sound='mewo meow'

def All_Sounds(obj):
    #1 if hasattr(obj, 'sound'):
    #     obj.sound()
    
    if hasattr(obj, 'sound') and callable(obj.sound):
        obj.sound()


if __name__ == '__main__':
    for i in Duck(),Dog(),Cat():
        All_Sounds(i)

