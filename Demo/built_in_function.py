#help(it takes one arguments AND returns description of the arguments)
#map(it takes two arguments ,1st arguments is functiona nd second arguments is itetrable)
# elements=["1","2","445678","5","7456789"]
# print(list(map(len,elements)))
####filter(it takes two arguments 1st is function and it should return true a booloean value and 2nd arg is an itetrable)
jwells=["silver","gold","dimond","platinum"]

# def is_long(elm):
#     return len(elm)>5
# print(list(filter(is_long,jwells)))

###lamda function is also know as anonymous function ,it is a single line function it is mostly useful with map and filter function
#lamda arg:expression
# print(list(filter(lambda elm:len(elm)>5,jwells)))
# print(list(filter(lambda elm: "i" in elm,jwells)))
# print(list(map(lambda val:val.count("o"),jwells)))


# def right_words(lst,num):
#
#     return list(filter(lambda elm:len(elm)==num,lst))
# print(right_words(['cat', 'dog', 'bean', 'ace', 'heart'],3))
# print(right_words(['cat', 'dog', 'bean', 'ace', 'heart'], 5))
# print(right_words([], 4))


# def greater_sum(lst,lst1):
#    if  sum(lst)>sum(lst1):
#        return lst
#    elif sum(lst1)>sum(lst):
#          return lst1
#    else:
#        return lst==lst1
#
# print(greater_sum([1, 2, 4], [1, 2, 4]))

##all(it takes itetrable and checks if one value false then it will return false)
##any(it takes itetrable and checks if any of the value is true then it will return true)
##sum(it returns the sum of the itetrablle )
##min(returns minimum value of the itetrable)
##max(return max value from the itr)




