class Test:
    def __init__(self,pu,po,pr):
        self.pu=pu
        self._po=po
        self.__pr=pr
    def show(self):
        print(f'{self.pu} {self._po} {self.__pr}')
    def getPr(self):
        return self.__pr


t=Test(1,2,3)
t.show()
print(t.pu)
print(t._po)

try: 
    print(t.__pr)
except:
    print('Private variable cannot be accessed outside of the class') 

print(t._Test__pr)
print(t.getPr())