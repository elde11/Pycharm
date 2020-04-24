class MyClass:
    _protected_class_attribute = "ProtClassAttr"
    class_normal_attribute = "NormalAttribute"
    def public_methods(self):
        self._protected_method()
        print("wywolales metode publiczna")
    def _protected_method(self):
        print ("wywolales metode chroniona")
    def __init__(self):
        self.object_normal_atrribute = None
        self._protected_attribute = None #atrybut chroniony przez podłogę
    def get_protected_atr(self):
     #   self._protected_attribute
        return self._protected_attribute
    def set_protected_atr(self, new_value):
        self._protected_attribute = new_value
x = MyClass()
print(x.get_protected_atr())
x.set_protected_atr(5)
print(x.get_protected_atr())
x.public_methods()