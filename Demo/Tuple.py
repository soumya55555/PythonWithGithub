#Tuple is imutable ,fixed size
# tup="Jan","Feb","March"
# print(type(tup))
#
# tup1=(1,)
# print(type(tup1))

##################Tuple Unpacking############################
employee=("bob","jonson","manager",45)
# first_name,last_name,position,age=employee
# print(first_name)
# print(last_name)
# print(position,age)

# first_name,last_name,*details=employee####any number of value in astrick will return a list
# print(first_name,last_name)
# print(details)


# *names,position,age=employee
# print(names)


# first_name,*position,age=employee
# print(position)



# def sum_of_evens_and_odds(tup):
#
#     lst_odd=[]
#     lst_even=[]
#     for i in tup:
#         sum = 0
#         if i%2==0:
#             sum=sum+i
#
#             lst_even.append(sum)
#
#             #print(lst_even)
#         else:
#             sum += i
#             lst_odd.append(sum)
#
#     lst3=lst_even+lst_odd
#
#     return tuple(lst3)
#
#
# print(sum_of_evens_and_odds((1, 2, 3, 4)))







lst=[5,5]

def s(a,b,*c):
    print(type(c))
    print(a+b)
s(*lst)

#positional arguments ie *args return a class of tuple