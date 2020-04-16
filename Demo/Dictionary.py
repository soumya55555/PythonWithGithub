#dictionary is a unordered data structure,it has key and value pair.
#key is immutable object like tuple,int,float,string
#value can be any of data structure
#key will be always a unique
#value can be dupilicated
# dic={("sam","ria"):[20,30],"Phone_number":[3456789,345890],"Organization":"Google"}
# print(type(dic))
# # print(len(dic))
# # print(dic[("sam","ria")][1])
# print(dic.get("Phone_number"))
# print(dic.get(3,"Not avialbe"))#if the key is not persent in the dict then it will return the default value ,it wont through error
# print(dic.get(9))#if we will not provide 2nd oarameter then it will return none


# natural={
#
# }
# natural["fruits"]=["apple","mango","grapes","orange"]
# natural["vegies"]=["cauliflower","cabbage","spinach"]
# natural["flowers"]=["rose","jasmine","hibiscuss"]
# print(natural)
# print(natural["fruits"][1])
# natural["vegies"][0]="potato"
# print(natural)

# words=["love","india","india","country"]
# def count_word(words):
#     count={}
#     for word in words:
#         if word in count:
#             print(count[word])
#             count[word]+=1
#         else:
#             count[word]=1
#
#     return count
#
# print(count_word(words))

# print(natural)
# natural.setdefault("dryFruits",["almonds","rinses","casew","chia seeds"])
# print(natural)

dryFruits= ['almonds', 'rinses', 'casew', 'chia seeds']



# def to_dictionary(lst):
#     count={}
#     for i in dryFruits:
#         count[i]=dryFruits.index(i)
#     return count
#
# print(to_dictionary(dryFruits))
# del dryFruits[2]
# print(dryFruits)
#--------------------------------------------------------------------#
#POP and del
# years={
#     "python":1991,
#      "java":1995,
#       "ruby":1995
# }

# last=years.pop("ruby")
# print(last)
# last=years.pop("c++",2000)
# print(last)
# years.pop("ruby")
# print(years)
#
# del years["ruby"]
# print(years)
# del years
# print(years)

# my_dict = {
#   "A": 1,
#   "B": 2,
#   "C": 3
# }
# strings = ["A", "C"]
# def delete_keys(dic,str):
#
#     for i  in str:
#         if i in dic:
#             del dic[i]
#
#
#
#     return dic
# print(delete_keys(my_dict,strings))


# tv_shows={
#     "BigBoss":{
#         "Season12":{
#             "contestant":["deepika","sresanth","anup","jashleen"],
#             "host":"Salman Khan",
#             "Ratings":0
#         },
#         "seasons13":{
#             "contestant":["sidharth","sehenaaz","paras","rasmi","mahira"],
#             "host_of_the_season":"The salman khan",
#             "ratings":5,
#             "Winner":"*Sidharth sukla*"
#         },
#         "Seasons14":{
#             "contestant":"Unknown",
#             "Host":"Salman",
#             "ratings":"To be decided"
#         }
#     }
# }
# print(tv_shows["BigBoss"]["seasons13"]["Winner"])



#Which method merges a dictionary with another one?(update method merges )

# What are the differences between the get and setdefault methods?
#
# If a key is not found in a dictionary, the get method will return its second argument as the value.
#
# In comparison, if a key is not found in a dictionary,
# the setdefault method writes the key-value pair to the dictionary.
# The first argument to the method will serve as the key and the second argument will serve as the value. The second argument has a default argument of None.


# pounds_to_kilogram={
#     5:2.26796,
#     10:452539,
#     25:113398
# }
# for pound in pounds_to_kilogram:
#     print(f"The pound {pound} is equal to {pounds_to_kilogram[pound]} ")

#item() unpack the dictionary
# my_dict = {
#   "A": "B",
#   "C": "D",
#   "E": "F"
# }
# def invert(dic):
#     dic_inverted={}
#     for key,value in dic.items():
#         dic_inverted[value]=key
#     return dic_inverted
#
# print(invert(my_dict))
# my_dict = {
#   "A": "K",
#   "B": "D",
#   "C": "A",
#   "D": "Z"
# }

#
# def common_elements(dic):
#     lst=[]
#     for elements in  dic.keys():
#         for j in dic.values():
#             if elements in j:
#                 lst.append(j)
#     return lst
#
#
# print(common_elements(my_dict))

# attentides_concert=[
#     {"name":"Salman","amount":1234567890,"duration":1},
#     {"name":"SRK","amount":12345678,"duration":1},
#     {"name":"kajol","amount":12345678,"duration":1}
# ]

# for attenddie in attentides_concert:
#     for key,value in attenddie.items():
#         print(f"The {key} is  {value}")
#*arg(positional argument,it returns a tuple)
#**kwargs(keyword arguments,it returns a dictionary)
# def args_and_kwargs(a,b,*args,**kwargs):
#     print(f"sum of two numbers is {a+b}")
#     print(f"sum of positional args is {sum(args)}")
#     sum1 = 0
#     for value in kwargs.values():
#         sum1+=value
#     print(f"sum of keyword aruguments is {sum1}")
#
# args_and_kwargs(1,2,3,4,5,6,x=10,y=20,z=30)

# #unpacking a dictionary
# total={
#     "num1":20,
#     "num2":30
# }
# #kwargs unpacks dictionary
#
#
# def total_sum(num1,num2):
#     return num1+num2
# print(total_sum(**total))

def plenty_of_arguments(a,b,**kwargs):
    sum_total_value = 0
    num=kwargs.values()
    #print(sum(num))
    sum_total_value= a+b+sum(num)


    if sum_total_value>100:
        return True
    else:
        return False


print(plenty_of_arguments(a = 50, b = 25, c = 50))
print(plenty_of_arguments(a = 25, b = 25, c = 25, d = 26))

#**kwargs returns a dictionary