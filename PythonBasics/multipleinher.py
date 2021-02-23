class Base1(object):
    def __init__(self):
        self.str1="Hello"
        print("Base1")

class Base2(object):
    def __init__(self):
        self.str2="Python"
        print("Base2")

class child(Base1,Base2):
    def __init__(self):
        Base1.__init__(self)
        Base2.__init__(self)

        print("i Ma the child")

    def printstrings(self):
        print(self.str1,self.str2)


ob=child()
ob.printstrings()



print("\n ")
class parent(object):

    def __init__(self,x):
        self.x=x

class children(parent):
    def __init__(self,x,y):
        parent.x=x
        self.y=y

    def print(self):
        print(self.x,self.y)

o=children(10,20)
o.print()