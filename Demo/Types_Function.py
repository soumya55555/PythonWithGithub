#Parameter and agmenent function
# def add(text):
#     print(text)
#
# add("heloo world")

#Positional and keyword arguments
# def add_number(a,b,c):
#     print("add  numbers and display the result ", a+b+c)
#
#
# # add_number(10,20)
# # add_number(a=20,b=30)
# add_number(a=20,b=30)

#Default arguments
# def string_adder(a=" ",b =" "):
#     print("print the value " , a +" "+ b)
#
# string_adder("soumya","pattanayak")
# string_adder()



#####function annotation########
def word_multipler(word:str,times:int) ->str:
    return word*times
print(type(word_multipler("hello",5)))