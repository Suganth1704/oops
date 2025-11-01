from abc import *
from accessSpecifiers import Test 
class Abs(ABC):
    @abstractmethod
    def show(self):pass

    def display(self):
        print("Display from abstract class")

# Above class is called the abstract class b'z it contiains both adstact and implemented method.

class Child(Abs):
    def show(self):
        print("Ab method implementation")

if __name__=='__main__':
    c=Child()
    c.display()
    c.show()
    t=Test(1,2,3)
    print(t.getPr())

"""
class Abs(ABC):

    @abstractmethod
    def show(self):pass

    @abstractmethod
    def display(self):pass
        

# The above one is called the interface b'z it contains only the abstract methods only in it.
Note: 
        Concrete method is the method with full implementation.

"""
