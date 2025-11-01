class Test:
    def show(self):
        print('Hi')
    def show(self,fname):
        print("Hi ",fname)
    def show(self,fname,lname):
        print("Hi {} {}".format(fname,lname))


if __name__=='__main__':
    t=Test()
    #t.show() # Test.show() missing 2 required positional arguments: 'fname' and 'lname'
    #t.show('Suganth')
    t.show('Suganth','Ajish kumar')