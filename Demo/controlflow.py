

# def even_or_odd(num):
#
#     if num%2==0:
#         return "Number is even"
#     else:
#         return "Number is Odd"
#
#
# print(even_or_odd(1))

# def up_and_down(word:str):
#     if word.islower()==True:
#         return word.upper()
#     elif word.isupper()==True:
#         return word.lower()
#     else:
#        return word.swapcase()
#
# print(up_and_down("Abcde"))
# print(up_and_down("asdfghjk"))
# print(up_and_down(("ASFHJKKK")))


zip_code="12345"
# if len(zip_code)==5:
#      print("Valid")
# else:
#     print("Invalid")
#################conditional expression####################
# check="Valid" if len(zip_code)==5 else "Invalid"
# print(check)
# input=int(input("Enter number"))
# even_check="Even Number" if input%2==0 else "Odd Number"
# print(even_check)

# num=int(input("Enter a number"))
# def divisible_by_three_and_four(num):
#     if num%3==0 and num%4==0:
#         return True
#     else:
#         return False



# print(divisible_by_three_and_four(num))


# num=int(input("Enter a number"))

def fizzbuzz(num):
  for i in range(num+1):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%5==0:
        print("Buzz")
    elif i%3==0 :
        print("Fizz")
    else:
        print(i)




fizzbuzz(30)






