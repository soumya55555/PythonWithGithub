# class Country():
#     pass
#
# india=Country()
# print(india)
# america=Country()
# print(america)

#####__init__()##########
##dunder init method is use to initialize an object
#it gets invoked when a class is instantiate
# class Fruit():
#     def __init__(self):
#         print(f"A new fruit is being introduced,and fruit is a {self}")
#
# apple=Fruit()
# print(apple)#both objects at one location
# orange=Fruit()
# print(orange)
# ##Adding attribute to object
# apple.price=200
# apple.colour="red"
# print(apple.colour)
# orange.taste="yumm"
# print(orange.taste)
# print(orange.colour)#AttributeError: 'Fruit' object has no attribute 'colour' bcoz orange object doesnt contain colour attribute,scope is only for apple object


#____________________________________#
# class Musical():
#     def __init__(self,name):
#         self.name=name
#         print(f"{name}")
#
# guitar=Musical("acoustic")
# electric=Musical("electric_guitar")
# # print(guitar.name)
# # print(electric.name)
#______________________________________________________#
# class Zombie():
#     def __init__(self,health=100,brains_eaten=5):
#         self.health=health
#         self.brains_eaten=brains_eaten
#         print(f"health is{health} and brain eaten {brains_eaten}")
#
# bob=Zombie(80)
# sally=Zombie(120,3)
# benjamin=Zombie()
# # print(bob)
# # print(sally)
# # print(benjamin)

####################################################
class Musician():
    def __init__(self,age,income):
        self.age=age
        self.income=income
    def describe(self):
        print(f"my age is {self.age} and my income is {self.income}")
    def enter_club(self):
        if self.age>21:
            return "Access granted!"
        else:
            return "Access denied!"
    def play_show(self):
        self.income+=5
        return self.income

# age_res=Musician(10,10000)
age_res=Musician(20,200005)
# age_res.describe()
age_res.describe()
print(age_res.enter_club())
print(age_res.play_show())
#if we declare two objects with same name then it wont through exception it will override the 1st declared value with latest one







