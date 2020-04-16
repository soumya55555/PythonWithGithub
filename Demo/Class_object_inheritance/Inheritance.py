# class Store():
#     def __init__(self):
#         self.owner="soumya"
#
#     def greet(self):
#         print(f"welcome to the store, i am {self.owner} ,owner of the shop")
#
# class HardwareStore(Store):
#     pass
# home_depot=HardwareStore()
# home_depot.greet()
# class Clothing():
#     def __init__(self):
#         print("hey there i am the super class")
#     def wear(self):
#         return "I'm wearing this fashionable piece of clothing!"
#     def sell(self):
#         return "Buy my piece of clothing!"
#
# class Socks(Clothing):
#     def __init__(self):
#         print("hey there i am the sub class")
#     def lose_one(self):
#         return "Where did my other one go?"
#     def wear(self):
#         return "Take a look at my socks! They're gorgeous!"
#     def sell(self):
#         return "Buy my socks!"
#
# clean_socks=Socks()
# print(clean_socks.wear())
# print(clean_socks.lose_one())
#####super is used to get the instance or return the instance of super class
class Musician():
    def __init__(self,name):
        self.name=name
        self.albums=[]
    def release_album(self,title:str):
        self.albums.insert(len(self.albums),title)

class Drummer(Musician):
    def __init__(self,name,stamina:int):
        super().__init__(name)
        self.stamina=stamina

lars = Drummer(name = "Lars", stamina = 2)
print(lars.name)
print(lars.stamina)
lars.release_album("Ride the Lightning")
print(lars.albums)
lars.release_album("Master of Puppets")
print(lars.albums)  # ["Ride the Lightning", 'Master of Puppets']