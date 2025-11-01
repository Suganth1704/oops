class Myclass:
    def __init__(self):
        self._proVar = 'Suganth'
        self.__priVar = '123456'

    def showPriVar(self):
        print(f'priVar : {self.__priVar}')
    

#cls method
class ClsMeth:
    mathOp = 0
    def __init__(self,):
        ClsMeth.mathOp += 1
        self.int = 2

    def __repr__(self):
        print(f'{self.int}')
    
    @classmethod
    def getMathOp(cls):
        return cls.mathOp

class Animal:

    def sound(self):
        return "Makes Sound o))"

class Dog(Animal):

    def sound(self):
        return "Wow WoW"

class Cat(Animal):

    def sound(self):
        return "Meow Meow"



