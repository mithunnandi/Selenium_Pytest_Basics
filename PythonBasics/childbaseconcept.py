class Base(object):
    pass #Empty class

class Child(Base):
    pass

class Child1():
    pass

print(issubclass(Child,Base))
print(issubclass(Base,Child))
print(issubclass(Child1,Base))

b=Base()
c=Child()

print(isinstance(b,Base))
print(isinstance(c,Child))
