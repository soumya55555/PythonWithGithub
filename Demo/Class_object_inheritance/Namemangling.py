class Vechile():
    def __init__(self):
        self.__some_attribute="hello"

    def __some_method(self):
        print("this is a private method from vechile class")



class Car(Vechile):
    pass

v=Vechile()
c=Car()
# print(v._Vechile__some_attribute)
# print(c._Vechile__some_attribute)
c._Vechile__some_method()
v._Vechile__some_method()

#name mangling basicaly useed to remove the conflict between two classes and there attribute and methods