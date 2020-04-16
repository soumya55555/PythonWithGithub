# empty=[]
# active=[True]
# favorite_numbers=[2,4,6,8,10]
# colors=["red","green","blue"]
# def is_long(lst):
#     if len(lst)>=5:
#         return True
#     else:
#         return False
#
# print(is_long([1,2,3,4,5,6]))


# def first_and_last(lst):
#     return lst[0]+lst[len(lst)-1]
#
# print(first_and_last([1,2,3,4]))
# print(first_and_last(["a","b","c"]))
# print(first_and_last(["bob", "tom", "rob"]))
# print(first_and_last(["a"]))


# values = ["a", "b", "c", "d", "e", "f"]
# def split_in_two(lst,num):
#     if num%2==0:
#         return lst[2:]
#     else:
#         return lst[0:2]
#
# print(split_in_two(values,4))
# print(split_in_two(values,1))
# print(split_in_two(values,10))
#
#
# print(values[1])



# nl = [[3, 4, 5],[7, 8, 9],[10, 11, 12]]
#
# def nested_extraction(lst,index):
#     return (lst[index][index])
#
# print(nested_extraction(nl,2))


# def sum_of_lengths(lst):
#     sum=0
#     for i in lst:
#
#      sum=sum+len(i)
#
#     return  sum
#
#
# print(sum_of_lengths(["Nonsense", "or", "confidence"]))

# def smallest_number(lst):
#     smallest=lst[0]
#     largest=lst[0]
#     for i in lst:
#         if i>largest:
#             largest= i
#
#         elif i<smallest:
#             smallest=i
#     print("smallest number is ",smallest)
#     print("largest number in the list is ",largest)
#
# smallest_number([1,20,30,10,2,3,40])

# def in_list(lst,str:str):
#     for index,value in enumerate(lst):
#         if str in lst:
#             print(f"{value} present in the list , {index} position")
#             return 1
#         else:
#             print(f"{value}  not present in the list ")
#             return -1
#
#
# print(in_list(["enchanted", "sparks fly", "long live"],"enchand"))
# for index, num in enumerate([1, 1, 2, 2, 5]):
#     if index > num:
#         break
#
#     print(num)

# for index, num in enumerate([1, 1, 2, 2, 5]):
#     if index < num:
#         continue
#
#     print(num)

def length_match(lst,num):
    count = 0
    for value in lst:

        if len(value)==num:
           count+=1
    return count

# print(length_match(["cat", "dog", "kangaroo", "mouse"], 3))
# print(length_match(["cat", "dog", "kangaroo", "mouse"], 4))




lst=[3,4,3,5,3,6]

def check(lst:list):
    lst1=[]
    sum=1
    for i in lst:
      if lst.index(i)%2==0:
          lst1.append(i)
    #return lst1*sum
    #print(lst1)
    for i in lst1:
        sum*=i
        #sum=sum*i
    return sum







print(check(lst))
# lst=[1,3,5]
# sum=1
# for i in lst:
#     sum*=i
#     print(sum)


