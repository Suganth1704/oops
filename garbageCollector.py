import time
import gc
class Student:
    def __init__(self):
        print("Object initialization")
    def __del__(self):
        print("Destructor is initalized")


if __name__=='__main__':
    # s=Student()
    # s1=Student()
    s1=[Student(),Student(),Student()]
    del s1
    time.sleep(5)
    print("End of the Application")
    
    """
    gc.isenabled()
    gc.enable()
    gc.disable()

    """