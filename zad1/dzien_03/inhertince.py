#class BaseClass:
#   pass
#
#class DerivedClass(BaseClass):
 #   pass


 class Base:
     def __init__(self):
         self.name = 'Base'
         print("I'm base class")

    def fun(self):
        print(f"Base class fun{self.name}")

b = Base()
b.fun()

class Derived1(Base)
    def __init__(self):
        self.name = "derived"
        print("I'm derived class One")

    def not_so_funny(self):
        pass

d = Derived1()
d.fun()