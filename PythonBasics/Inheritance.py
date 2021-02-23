class Person(object):

    def __init__(self,name):
        self.name=name

    def getname(self):
        return self.name

    def isemployee(self):
        return False

class employee(Person):

    def isemployee(self):
        return True


emp=Person("mithun")
print(emp.name)
print(emp.getname(),emp.isemployee())

#Child inheiting properties from Parent

emp1=employee("Peter")
print(emp1.name)
print(emp1.getname(),emp1.isemployee())



