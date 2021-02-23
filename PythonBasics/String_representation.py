print("String representation of class concept")
print("Object printing concept")

class test:

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __repr__(self):
        return "x:%s y:%s" % (self.x, self.y)
    def __str__(self):
        return "value of x is :%s value of y is:%s" %(self.x,self.y)
#Ideally str method will be printed by default (if noth str and repr method are defined ),if str method is not defined then repr method will be executed

t=test(1,2)
print(t)