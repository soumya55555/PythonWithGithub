def add(a,b):
    return a+b
def substract(a,b):
    return a-b


def calculate(func,a,b):
    return func(a,b)


print(calculate(add,3,4))
print(calculate(substract,10,4))

######NESTED Function##################
def convert_gallons_to_cups(gallons):
    def convert_gallons_to_squart(gallons):
        print(f"Converting {gallons} gallons to squart!")
        return gallons*4
    def convert_squart_to_pints(squart):
        print(f"Converting {squart} squart to pints!")
        return squart*2
    def convert_pints_to_cups(pints):
        print(f"Converting {pints} pints to cups!")
        return pints*2
    quarts=convert_gallons_to_squart(gallons)
    pints=convert_squart_to_pints(quarts)
    cups=convert_pints_to_cups(pints)
    return cups
print(convert_gallons_to_cups(4))


######################
def Calculator(operation):
    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
    if operation=="add":
        return add
    elif operation=="sub":
        return sub



print(Calculator("add")(10,20))
print(Calculator("sub")(10,10))



###################################################
##Store functions in a list
def squre(num):
    return num**2
def cube(num):
    return num**3
def times10(num):
    return num*10

operations=[squre,cube,times10]
for operation in operations:
    print(operation(5))


####global and local varibale
age=20
def x():
    age=29

#if same name exist for local and global varibale the it's called shadow varibale'
#python works with LEGB
#Local/enclosing function/global/builtin
def outer():
    x=10#Enclosing
    def inner():
        #x=20
        return len
    return inner()
print(outer()("python"))

###global and nonlocal(enclosing function scope) keyword

##Decorators in python -function that takes a function and return an another function
# def be_nice(fn):
#     def inner():
#         print("welcome to this world,we are happy to execute your code")
#         fn()
#         print("Thank you for visting us,we will look forward to work for you ")
#     inner()
#
#
#
# @be_nice
# def complex_to_code():
#     print("****complex can be tackle easily****")
#
# # print(be_nice(complex_to_code))
# #be_nice(complex_to_code)
# @be_nice
# def fancy_function_to_showcase():
#     print("*************happy in fancy function***************")


# def lets_decorate(fnc):
#     def inner_decoration(*args,**kwargs):
#         print("Welcome,How can i help you with your code?")
#         fnc(*args,**kwargs)
#         print("Thank you for giving us a chance to treate  you .*.")
#     return inner_decoration
#
#
# @lets_decorate
# def designer(name):
#     print(f"it was very difficult to decorate for {name} ,but we did it")
#
# designer("boris")

def lets_decorate(fnc):
    def inner_decoration(*args,**kwargs):
        print("Welcome,How can i help you with your code?")
        results=fnc(*args,**kwargs)
        print("Thank you for giving us a chance to treate  you .*.")
        return results

    return inner_decoration

@lets_decorate
def complex_sum(a=10,b=20):
    return a+b
print(complex_sum())








