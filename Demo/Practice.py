# s="Stress"
# lst=[]
# for i in s:
#     if i
#
# s="Madhusmita"
# dic=dict()
# for char in s:
#     lst=["a","e","i","o","u"]
#     for i in lst:
#         if char ==i:
#
#             if char in dic:
#                 dic[i]+=1
#             else:
#                 dic[i]=1
#
#
# print(dic)
from builtins import type
from symbol import return_stmt

lst1=[1,2,3,4,5,6]
#
size=len(lst1)
# temp=lst1[0]
# lst1[0]=lst1[size-1]
# lst1[size-1]=temp
# print(lst1)
# temp=lst1[0:2]
# lst1[0:2]=lst1[-2:]
# lst1[-2:]=temp
# print(lst1)

# def check(lst,word,Nth):
#     newlist=[]
#     count=0
#     for i in lst:
#         if(i==word):
#             count=count+1
#             if(count!=Nth):
#                 newlist.append(i)
#             else:
#                 lst.remove(i)
#     lst=newlist
#     if count==0:
#         print("item not found")
#     else:
#         print("updated list is:",lst)
#         return newlist
#
#
# check(["can", "you",  "can", "a", "can" "?"],"can",1)
#
# def count_occurance(lst):
#     newlist=[]
#     count=0
#     for value in lst:
#         if value in newlist:
#             count+=1
#         else:

# x=10
#
# count=0
# lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]
#
# for i in lst:
#     if i==x:
#         count=count+1
#
#
# print(count)
#x="google"
# lst=list(x)
# lst1=[]
# for i in x:
#     count=lst1.count(i)
#     print(count)
#     if i in lst1:
#         if count>1:
#          lst1.remove(i)
#     else:
#         lst1.append(i)
#
#
#
#
#
# print(lst1)
#print(dir(x))

# lst_num=[1,2,3,4,5,6,7]
# sum=1
# for i in lst_num:
#     sum*=i
# print(sum)
# lst=[0,1,2,3,4,5,6,7,8]
# smallest = lst[0]
# largest = lst[0]
# second_largest=lst[0]
# for num in lst:
#     if num>largest:
#         largest=num
#         second_largest=largest-1
#     elif num<smallest:
#         smallest=num
#
#
# print("smallest number from the list:",smallest)
# print("largest number from the list:",largest)
# print("second largest number:",second_largest)

# even_lst=[]
# odd_lst=[]
# for num in range(0,100):
#     if num%2==0:
#         even_lst.append(num)
#     else:
#         odd_lst.append(num)
# print("This list consisting of even numbers:", even_lst)
# print("This list consisting of odd numbers:", odd_lst)
# lst=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# for num in lst:
#     if num%2==0:
#         even_lst.append(num)
#     else:
#         odd_lst.append(num)
# print("Number of even numbers from the list:",len(even_lst))
# print("Number of odd numbers from the list:",len(odd_lst))


# lst=[1,2,3,1,2,3,4,5,6,7,1,2]
# for i in lst:
#     if lst.count(i)>1:
#         lst.remove(i)
#
# print(lst)
# lst=[1,2,(3,4,56),(),(),[],{}]#all blank objects are false
# # def rmv(tup):
# #     tup=[t for t in tup if t]
# #     return tup
# #
# # print(rmv(lst))
#
#
# for t in lst:
#     if t==True:
#         print(t)
#     else:
#         print(t)

# numbers=[1,23,65,23,15,16,25,15,15]
# dup_num=[]
# for num in numbers:
#     if numbers.count(num)>1:
#         dup_num.append(num)
# print("duplicate numbers in a list :" ,dup_num)


#Sort the values of first list using second list
# lst1=[8,7,2,6,10]
# lst2=[1,2,3,4]
# x = ["g", "e", "e", "k", "s", "f", "o", "r", "g", "e", "e", "k", "s"]
# y = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]
# # print(sorted(zip(lst1,lst2)))
# sorted_list=sorted(zip(y,x))
# ls=[i for i in sorted_list]doubttttt
# print(ls)
#


#Python program to check if a string is palindrome or not
# str=input("Enter the string ")
# def check_rev(str):
#     if str==str[::-1]:
#         print("string is a palindrome:",str)
#     else:
#         print("string is not a palidrome:",str)
#
#
# check_rev(str)
#Find length of a string in python (4 ways)
# str="soumya"
# print(len(str))
# counter = 0
# for i in str:
#     counter+=1
# print(counter)


#Python program to print even length words in a string
# str="i love my india"
# str1=str.split(" ")
# #print(str1)
# for i in str1:
#     if len(i)%2==0:
#         print(i)
#Program to accept the strings which contains all vowels
# def check_vowel(str):
#     if str in  "aeiouAEIOU":
#         print("string accepted")
#     else:
#         print("string rejected")
#
# check_vowel("geeksforgeeks")
# check_vowel("ABeeIghiObhkUul")


#Count the Number of matching characters in a pair of string
# str="i love my india i love  python"
# str1=str.split(" ")
# dic=dict()
# for char in str1:
#     if char in dic:
#         dic[char]+=1
#     else:
#         dic[char]=1
#
# print(dic)

#program to count number of vowels using sets in given string
# def func_vow(str):
#  vowels={"a","e","i","o","u","A","E","I","O","U"}
#  counter=0
#  for i in vowels:
#      for j in str:
#          if j ==i:
#              counter+=1
#  return counter
#
# print(func_vow("soumya"))
# print(func_vow("elePhANtAAa"))


#Remove all duplicates from a given string in Python
# def remove_duplicate(str:str):
#     lst=[]
#     for i in str:
#         lst.append(i)
#         if lst.count(i)>1:
#             lst.remove(i)
#             return lst
#
# print(remove_duplicate("soumyapattanayak"))
# print(remove_duplicate("geeksforgeeks"))


# Find words which are greater than given length k
# lst=["abcde","abc","soumyaa","xyz123"]
# lst1=[i for i in lst if len(i)>5]
# print(lst1)

#Python program to split and join a string
# str="Geeks for Geeks"
# lst=str.split(" ")
# print(lst)
# str1="_".join(lst)
# print(str1)

#Python | Check if a given string is binary string or not
# def check_Binary(str):
#     if "0" and "1" in str:
#         print("Given string is a binary")
#     else:
#         print("Given string does not have binary ")
#
#
# check_Binary("01010101010")



#Find all close matches of input string from a list
# from difflib import get_close_matches
# def pattern_matches(pattern,word):
#     print(get_close_matches(word,pattern))
#
# word = 'appel'
# patterns = ['ape', 'apple', 'peach', 'puppy']
# pattern_matches(patterns,word)

#program to find uncommon words from two Strings
# A = "Geeks for Geeks"
# B = "Learning from Geeks for Geeks"
# A=A.split(" ")##
# B=B.split(" ")

#Sort Python Dictionaries by Key or Value
dic={"name":"soumya","age":25,"phone":"redmi"}
# for value in dic.values():
#     print(value.)

print(10/0)





































