#Encapsulation is concept of data security,data protection
#Enclose the data with functions is called encapsulation
#to declare a varibale proteted _variable name
#The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
# class SmartPhone():
#     def __init__(self):
#         self._company="Apple"
#         self._firmware=10.0
# ipnone=SmartPhone()
# print(ipnone._company)
# print(ipnone._firmware)

# class Book():
#     def __init__(self,author, publisher,page_count):
#         self._author=author
#         self._publisher=publisher
#         self.page_count=page_count
#     def copyright(self):
#         print(self._author,self._publisher)
#
#
#     def rip_in_half(self):
#         if self.page_count>1:
#             return 1
#         else:
#             return 0.0
# book=Book(author = "Grant Cardone", publisher = "10X Enterprises", page_count = 10)
# book.copyright()
# print(book.rip_in_half())
# class Currency():
#     def __init__(self,dollar):
#         self._cent=dollar*100
#
#     def _get_dollar(self):
#         return self._cent/100
#     def _set_dollar(self,dollar):
#         if self.dollar>0:
#          self._cent=dollar * 100
#     dollar=property(_get_dollar,_set_dollar)
# cur=Currency(10)
# cur.dollar=20
# print(cur.dollar)
# #print(cur._get_dollar())
#with decorators
# class Currency():
#     def __init__(self,dollar):
#         self._cent=dollar*100
#     @property
#     def dollar(self):
#         return self._cent/100
#     @dollar.setter
#     def dollar(self, dollar):
#         if self.dollar>0:
#          self._cent=dollar * 100
# cu=Currency(50000)
# print(cu.dollar)

# class PizzaPie():
#     def __init__(self,total_slices):
#        self._slices_eaten=total_slices
#
#     def _get_slices_eaten(self):
#         return self._slices_eaten
#     def _set_slices_eaten(self,total_slices):
#         if self._slices_eaten<total_slices:                    ##########doubts###########
#                 self._slices_eaten
#
#     def percentage(self):
#         return self._slices_eaten/self.total_slices
#
#     total_slices=property(_get_slices_eaten,_set_slices_eaten)
# cheese = PizzaPie(8)
# cheese.slices_eaten = 2
# print(cheese.percentage())

#####getattr and setattr -get attribute and set attribute
starts={
    "name":"BBQ chicken",
    "price":300,
    "size":"large",
    "ingredients":["chicken","onion","bbq chicken"]
}
class Pizza():
    def __init__(self,starts:dict):
        for key,value in starts.items():
            setattr(self,key,value)

bbq=Pizza(starts)
print(bbq.name)
print(bbq.ingredients)
for attr in ["name","size","lenghth","discount"]:
    print(getattr(bbq,attr,"not defined"))

starts_to_delete=["size","diameter","abcd"]
for start in starts_to_delete:
    if hasattr(bbq,start):#hasattr returns true if the attribute present in the object
        print(start)
        delattr(bbq,start)#delattr delete the attribute if present in the object