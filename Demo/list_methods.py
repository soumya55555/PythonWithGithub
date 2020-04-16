# lst=[1,20,30,300,220,101]
# lst.append(102)
# print(lst)
# lst.extend([10,103,302,402])
# print(lst)
# lst.insert(1,"hello")
# print(lst)
# lst.remove(30)
# print(lst)
# last=lst.pop()
# print(lst)
# print(last)
# del lst[3]
# print(lst)
# # del lst[100]
# # print(lst)
#
# lst1=lst.pop(4)
# print(lst1)
# print(lst)
# #lst.clear()
# lst.reverse()
# print(lst)

# def word_lengths(str):
#
#     lst=str.split(" ")
#     print(lst)
#     lst1=[]
#
#     for i in lst:
#         lst1.append(len(i))
#
#     print(lst1)
#
#
#
# word_lengths("Mary Poppins was a nanny")

# st="Mary Poppins was a nanny"
# # lst=st.split(" ")
# # print(len(lst))
# print(" ".join(st))
#
#
#
# phn_number=["5555","4444","3333","2222","1111"]
# print(" - ".join(phn_number))

####ZIP function######
# breakfast=["egg","boiled chicken","bread"]
# lunch=["noodles","chicken pasta","juice"]
# dinner=["vegitable salad","dry fruits","meat"]
# print(zip(breakfast,lunch,dinner))
# print(type(zip(breakfast,lunch,dinner)))
# print(list(zip(breakfast,lunch,dinner)))
#
# for bf,ln,dn in zip(breakfast,lunch,dinner):
#     print(f"my breakfast  : {breakfast} and  lunch :{lunch} and  dinner :{dinner} for today")



###3Multidimensional list
# def nested_sum(lst):
#     sum = 0
#     for i in lst:
#
#         for j in i:
#            #print(j)
#            sum=sum+j
#     return sum
#
#
#
#
# print(nested_sum([[1, 2, 3], [4, 5]]))
# print(nested_sum([[1, 2, 3], [], [], [4], [5]]))
# print(nested_sum([[]]))

####################list comprehension###################################
# The floats variable should store the floating point values for each string in the values list.
# values = ["3.14", "9.99", "567.324", "5.678"]
# floats =[float(value) for value in values]
# print(floats)

# The letters variable should store a list of 5 strings.
# Each of the strings should be a character from name concatenated together 3 times.
# i.e. ['BBB', 'ooo', 'rrr', 'iii', 'sss']
# name = "Boris"
# letters = [name_index*3 for name_index in name ]
# print(letters)

# The 'lengths' list should store a list with the lengths
# of each string in the 'elements' list
# elements = ["Hydrogen", "Helium", "Lithium", "Boron", "Carbon"]
# lengths = [len(element) for element in elements]
# print(lengths)

# lst=[1,2,3,4,5,6,7,8,9]
# even_num=[even**2 for even in lst if even%2==0]
# print(even_num)


lst=[1,2,3,4,5,6,4,5]
lst1=[]
for i in lst:
    if i not in lst:
        lst1.append(i)

print(lst1)











