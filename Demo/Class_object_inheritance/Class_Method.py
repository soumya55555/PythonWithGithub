#class method takes a cls  argumets rather than a class instance
# class FoodCoorner():
#     def __init__(self,mashroom,chicken,paneer="anchari paneer"):
#         self.msshroom=mashroom
#         self.chicken=chicken
#         self.paneer=paneer
#     @classmethod
#     def comboMeal(cls):
#         return cls(mashroom="chilly mashroom",chicken="fry chicken",paneer="paneer tikka")
#     @classmethod
#     def specialThalli(cls):
#         return cls(mashroom="kadhai mashroom",chicken="curry")
# fd=FoodCoorner.comboMeal()
# print(fd.chicken)
# fd1=FoodCoorner.specialThalli()
# print(fd1.paneer)

# class Chocolate():
#     def __init__(self,cacao_content):
#         self.cacao_content=cacao_content
#     @classmethod
#     def sweet(cls):
#         return cls(cacao_content=30)
#     @classmethod
#     def semisweet(cls):
#         return cls(cacao_content=50)
#
#     @classmethod
#     def bittersweet(cls):
#         return cls(cacao_content=70)
#
#     @classmethod
#     def bitter(cls):
#         return cls(cacao_content=99)
#
# ch=Chocolate.sweet()
# print(ch.cacao_content)
# ch1=Chocolate.semisweet()
# print(ch.cacao_content)
# print(id(ch))
# print(id(ch1))
##class attribute
# class Counter():
#     count=0
#     def __init__(self):
#       Counter.count+=1
#     @classmethod
#     def create_two_count(cls):
#          create_two=[cls(),cls()]
#          print(f"number of counter object created {cls.count}")
#          return create_two
#
# c=Counter.count
# print(c)
# c1=Counter()
# print(Counter.count)
# c2,c3=Counter.create_two_count()
# print(Counter.count)

##########static method
##it does not take cls argument or cls istance
class Squre():
    @staticmethod
    def make_squre(sqr):
        return sqr**2
    def s(self):
        print("sdf")
print(Squre.make_squre(4))




