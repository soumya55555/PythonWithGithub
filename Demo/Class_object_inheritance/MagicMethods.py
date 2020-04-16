#Everything in python is a object .
#so all objects have there own methods
# print(3.0+4.0)
# print(3.0.__add__(4.0))
# print(len([1,2,3,4]))
# print([1,2,3,4].__len__())
# print("h" in "hello")
# print("hello".__contains__("h"))
# print("python"[2])
# print("python".__getitem__(2))

# class Card():
#     def __init__(self,name,num):
#         self.name=name
#         self.num=num
#
#     def __str__(self):#it represents string value of an objects
#         return f"{self.name} of {self.num}"
#     def __repr__(self):#it represents the object representation of a class
#         return f'Card("{self.name}","{self.num}")'
#
# c=Card("king",1)
#
# print(c)
# print(repr(c))
# #print(c.__repr__())

# class Student():
#     def __init__(self,math,history,science):
#         self.math=math
#         self.history=history
#         self.science=science
#
#     def grade(self):
#         return self.math+self.history+self.science
#
#     def __eq__(self, others_student):
#         return self.grade()==others_student
#     def __add__(self, others_student):
#         return self.grade() + others_student.grade()
#
#     def __gt__(self, others_student):
#         return self.grade()>others_student.grade()
#     def __ge__(self, others_student):
#         return self.grade()>=others_student.grade()
#     def __lt__(self, others_student):
#         return self.grade()<others_student.grade()
#
#
# mark=Student(70,90,85)
# sam=Student(90,90,100)
# joe=Student(95,100,85)
# #print(sam.grade()==joe.grade())
# print(sam==joe)
# print(sam==mark)
# print(sam!=mark)
# print(sam+mark)
# print(sam>joe)
# print(mark>=joe)
# print(joe<mark)

class BusTrip():
    def __init__(self,destination,company,price):
        self.destination=destination
        self.company=company
        self.price=price
    def __str__(self):
        return f"You paid {self.price} to {self.company} to go to {self.destination}."
    def __sub__(self, other_trip):
        return self.price-other_trip.price
    def __eq__(self, other_trip):
        if self.destination==other_trip.destination :
            if self.__sub__(other_trip)<=3:
                return f"Same destination {self.destination} and price range between them is {self.__sub__(other_trip)}"


boston1 = BusTrip(destination = "Boston", company = "Greyhound", price = 24.99)
boston2 = BusTrip(destination = "Boston", company = "Megabus", price = 22.99)
boston3 = BusTrip(destination = "Boston", company = "Megabus", price = 49.99)
philly = BusTrip(destination = "Philadelphia", company = "Peter Pan", price = 12.99)


print(boston1)
#print(boston1 == philly)  # False - different destinations
print(boston1 == boston2)
print(boston3-boston1)
