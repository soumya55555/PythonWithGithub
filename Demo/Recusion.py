#recursion:when a function calls itself

# def count_down_from(num):
#     start=num
#     while start > 0:
#         print(start)
#         start-=1

# def count_down_from(num):
#     if num<=0:
#         return
#     print(num)
#     count_down_from(num-1)
#
#
# count_down_from(-5)

# def reverse(str:str):
#     print(str)
#     reverse(str)
#
# reverse("soumya")

# def reverse(str):
#     start_index=0
#     end_index=len(str)-1
#     reversed_string=""
#
#     while end_index>=start_index:
#         reversed_string=reversed_string+str[end_index]
#         end_index-=1
#     return reversed_string
#
# print(reverse("soumya"))
# def reverse(str):
#     if len(str)<=1:
#         return str
#     return str[-1]+reverse(str[:-1])
#
#
# print(reverse("soumya"))

def check_fact(num):
    while num<=0:
        return
    check_fact()

