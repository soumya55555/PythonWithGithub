s="GOOGLE"
s1=set()
for i in s:
    s1.add(i)
print(sorted(s1))


nums=[-4,-3,-5,3,4,5]
squre={num**2 for num in nums}
#print(squre)


##set is mutable unorderd data structure
#it doesnt allowed duplicates value
#it doesnt contains mutable objects like list and dictionary


# def remove_duplicates(lst:list):
#     st=set()
#     for i in lst:
#         st.add(i)
#
#     return list(st)
# print(remove_duplicates([1, 2, 3, 4,4,4,4,0]))
num_of_set={1,2,3,4,5,6}
num_of_set.update([(10)])
#print(num_of_set)
#add-it adds the value to the set
#Update-it takes an itetraible as argument and adds to the set
#remove-it removes the element from the set,if the element doesnt exist in the set then it will give any error
#discard-it removes the element from the set,if the lememnt doesnt exist then it will simply pass it wont return any error

set1={1,2,3,4,5,7,10}
set2={1,2,9,11,21,23}
#print(set1^set2)
print(set1.intersection(set2))
print(set1&set2)
print(set1.union(set2))
print(set1|set2)
print(set1.difference(set2))
print(set1-set2)
print(set1.symmetric_difference(set2))
print(set1^set2)

