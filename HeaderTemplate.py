"""
Program             : Header
Author              : Erik Moore
Date Created        : 01/11/2020
Purpose             : To summerize in house test tools

Revision History    : 
Date        Author      Revision
12/19/19    Erik        Added Class Stuff

"""

#Imports Here

class Generic:
    def __init__(self):
        """Constructer"""
        
    def Func1(self):
        print("Func1 empty")

    def Func2(self):
        print("Func2 empty")
        
#main if run by itself
if __name__ == "__main__":
    Obj1 = Generic()
    Obj1.Func1()
    Obj1.Func2()