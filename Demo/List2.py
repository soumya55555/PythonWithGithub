# great_directors = ["Martin Scorsese", "Steven Spielberg", "Francis Ford Coppola"]
# great_directors[1]="Michael Bay"
# print(great_directors)
# # Given the transformers list below, overwrite “Bumblebee” with “Grimlock”.
# transformers = ["Optimus Prime", "Megatron", "Bumblebee", "Starscream"]
# transformers[2]="Grimlock"
# print(transformers)
# # Given the camping_trip_supplies list below, overwrite "Socks" with "Food".
# camping_trip_supplies = ["Socks", "Flashlight", "Tent", "Blanket"]
# camping_trip_supplies[0]="Food"
# print(camping_trip_supplies)
# # Given the tech_companies list below, overwrite the Microsoft, Blueberry, and IBM strings
# # with the strings “Facebook” and “Apple”. Use list slicing syntax.
# tech_companies = ["Google", "Microsoft", "Blackberry", "IBM", "Yahoo"]
# tech_companies[1:4]=["Facebook","Apple"]
# print(tech_companies)

lst=[1,2,3,4,5,6,7,8,9,10]
# def squre(lst):
#     sqt=[]
#     for i in lst:
#         sqt.append(i**2)
#     return sqt
# print(squre(lst))
# def convert_to_float(lst):
#     flt=[]
#     for i in lst:
#         flt.append(float(i))
#     return flt
# print(convert_to_float(lst))

# def even_or_odd(lst):
#     even_odd=[]
#     for i in lst:
#         if i%2==0:
#             even_odd.append("True")
#         else:
#             even_odd.append("False")
#
#     return even_odd
# print(even_or_odd(lst))
#
# def only_evens(lst):
#     new_list_of_even_number=[]
#     for i in lst:
#         if i%2==0:
#          new_list_of_even_number.append(i)
#
#     return new_list_of_even_number
# print(only_evens(lst))
# def factorial(num):
#     fact=1
#     for i in range(1,num+1):
#         fact*=i
#         print(fact)
#         #print(fact)
#     #return fact
# factorial(64)

def delete_all(lst,num):
     for i in  lst:
        if i==num:
          lst.remove(num)
     return lst


print(delete_all([4,4,4],4))


