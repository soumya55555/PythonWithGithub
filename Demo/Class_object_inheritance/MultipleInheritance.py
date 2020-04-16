# class HDFC():
#     def deposite(self):
#         print("deposite the amount in hdfc bank")
#
#     def withDraw(self):
#         print("withdraw money from hdfc")
#
# class SBI():
#     def withDraw(self):
#         print("withdraw money from sbi")
#
#
# class Customer(HDFC,SBI):
#     pass
#
# c=Customer()
# c.deposite()
# c.withDraw()
# print(Customer.mro())
#mro stands for method resolution order,it gives the structure of class that is being inherited
#------------------------------------------------------------------------
#Breadth first search and Deepth first search
#python always look for deepth first search,it goes depth of the class to check the existance of tyhe method or attribute
#breadth first search will look first  for the parent nodes then again move inside the parent class

#suppose we have class A as the parent class or super class.it has 3 sub classes B,C,D
#B consists of E and F ,C consists of G and H,D consisits of I and J
#Deepth first search--->A->B>E>F>c>G>h>D>I>J
#breadth first search--->a>b>c>d>e>f>g>h>i>j

###########################################################################
###dimond shape#####
# class A():
#     pass
# class B(A):
#     def demo(self):
#         print("printing from class b")
# class C(A):
#     def demo(self):
#         print("printing from class c")
# class D(B,C):
#     pass
# d=D()
# d.demo()
# print(D.mro())


# class A():
#     def dispatch(self):
#         return "apple"
#
#
# class B(A):
#     pass
#
#
# class C(A):
#     def dispatch(self):
#         return "banana"
#
#
# class D(B, C):
#     pass
#
#
# my_obj = D()
# print(my_obj.dispatch())
# print(D.mro())



#isinsatnce and issubclass
#isinstance takes two arguments the 1st one is the object or value and the 2nd one is the object or value belongs to
# print(isinstance(1,int))
# print(isinstance([1,2,3],list))
# print(isinstance({1,2,3,4},dict))
# print(isinstance((1,2,3,4),type((1,2,3,4))))
#issubclass checks the 1st atg is the subclass of 2nd arg if yes true if not false
class A():
    pass
class B(A):
    pass
print(issubclass(B,A))
print(issubclass(A,B))
print(issubclass(A,object))


###composition doubt
# print(type(str(10)))
# print(int("10"))
print(10//5)