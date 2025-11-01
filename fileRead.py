class EPSON:
    def show(self):
        print('globals()[p] converts the string into a object')

with open('file.txt','r') as s:
    p=s.readline()

print(f'{p} is a {type(p)}')

classname=globals()[p]
x=classname()
print(f'{x.__class__.__name__} is a {type(x)}')
x.show()
