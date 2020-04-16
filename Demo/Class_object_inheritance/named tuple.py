import collections
# gymExercise=collections.namedtuple("GymExercise",["name","weight","rips"])
# squrt=gymExercise(name="squrt",weight=165,rips=3)
# print(squrt)
# benchpress=gymExercise(name="Benchpress",weight=185,rips=5)
# print(benchpress)
# books=collections.namedtuple("Book",["name","author","price"])
# book1=books("chemistry","Bk publication",500)
# print(type(books))#books refer to a class type
# print(book1)
# book2=books("math","Bk publication",700)
# book3=books("science","dk publication",400)
# print(type(book3))
# class Check():
#     def __init__(self,*book):
#         self.book=book
#         self.librarian=[]
#
#     def __len__(self):
#         return len(self.book)
#
#
# b=Check(book1,book2)
# print(len(b))

#####getitem and setitem
# class Car():
#     def __init__(self,maker,model,year):
#         self.maker=maker
#         self.model=model
#         self.year=year
#
# class Dealership():
#     def __init__(self):
#         self.cars=[]
#     def accept_delivery(self,car):
#         self.cars.append(car)
#
#     def __getitem__(self, index):
#         return self.cars[index]
#     def __setitem__(self, index, value):
#         self.cars[index]=value
#
# f150= Car(maker = "Ford", model = "F-150", year = 2019)
# camry = Car(maker = "Toyota", model = "Camry", year = 2020)
# porsche = Car (maker = "Porsche", model = "911 Carrera", year = 2021)
#
#
# dealership = Dealership()
# dealership.accept_delivery(f150)
# dealership.accept_delivery(camry)
# dealership.accept_delivery(porsche)
# print(dealership[0].year)
# #dealership[0] = porsche
# for car in dealership:
#   print(car.maker) # Porsche, Toyota


class Newspaper():
    def __init__(self,pages:int,sections:dict):
        self.pages=pages
        self.sections=sections
    def __len__(self):
        return self.pages
    def __getitem__(self, index):
        return self.sections[index]
    def __eq__(self, other):
        if self.pages==other.pages:
            if self.sections==other.sections:
                return True
            else:
                return False
        else:
            return False



monday_sections = {
  "Politics": "A5",
  "Sports": "B2",
  "Entertainment": "C3"
}

tuesday_sections = {
  "Travel": "A5",
  "Cooking": "B2",
}

wednesday_sections = {
  "Classifieds": "A5",
  "Weddings": "B2",
  "Weather": "C3"
}

np1 = Newspaper(pages = 80, sections = monday_sections)
np2 = Newspaper(pages = 60, sections = tuesday_sections)
np3 = Newspaper(pages = 80, sections = wednesday_sections)

print(len(np1))        # 80
print(len(np2))        # 60
print(np1 == np2)      # False
print(np2 == np3)      # True -- both have 80 pages and 3 sections
print(np1["Politics"]) # "A5"
print(np2["Cooking"])  # "B2"
