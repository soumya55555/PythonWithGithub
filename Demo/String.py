# alp="abcdefghijklmnopqrstuvwxyz"
# print(len(alp))
# print(alp[0:])
# print(alp[:])
# print(alp[:-1])
# print(alp[0::4])
# print(alp[:-1:6])
# print(alp[0:5:2])
#find and index
#find and index method search for the element and return the index value.if the elememnt doesnt present then find returns -1 and index return a tracebck error.
# language="python"
# print(language.find("n"))
# print(language.find("yz"))
#rfind method will return highest index of the string

# def is_vowel(st):
#    return  st in ['a','e','i','o','u']
# def check_vowel(name):
#     count=0
#     for i in range(len(name)):
#         if is_vowel(name[i]):
#             count+=1
#     return count

# # print(check_vowel("aeroplane"))
# print(is_vowel("ae"))



# word="once upon a time"
# # print(word.capitalize())
# # print(word.casefold())
# # print(word.swapcase())
# # print(word.title())
# # print(word.isspace())
# print(word.strip("oncetime"))
# print(word.rstrip())
# print(word.isspace())
# def fancy_cleanup(text:str):
#     text1=text.strip()
#     text2=text1.replace("g","z")
#     text3=text2.replace(" ","!")
#     return text3
#
# print(fancy_cleanup("grade"))
# name="soumya"
# age=25
# subject="python"
# #word=f"my name is {name} and i am {age} year's old ,love to read {subject}"
word="my name is {name} and i am {age} year's old ,love to read {subject}"
print(word.format(name="soumya",age=25,subject="python"))



