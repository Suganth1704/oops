class Singleton:
    _instance = None
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

class PrImmu:
    pass
class Immut(PrImmu):
    def __init__(self, x,y):
        # self._x = x
        # self._y = y
        print(super())
        super().__setattr__('_x',x)
        super().__setattr__('_y',y)
    
    def __setattr__(self, key, value):
        raise AttributeError("You are not allowed to modify it")

    def __len__(self,):
        return 23 #"Kidding dude!!"