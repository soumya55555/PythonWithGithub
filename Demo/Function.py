# def greeting():
#     return "HI Python"
#
# print(greeting())


#####
#leap year\
# month_days=[0,31,28,31,30,31,30,31,31,30,31,30,31]
# def is_leap(year):
#     return year%4==0 and (year%100!=0 & year%400==0 )
#
# def days_in_month(year,month):
#     if not 1<= month <=12:
#         return "invalid month"
#     if month==2 & is_leap(year):
#         return 29
#
#     return month_days[month]
# print(is_leap(2020))
# print(days_in_month(2020,5))






###########################
# def change(str):
#     str= str + " Hi hows you"
#     print(str)
#
# String1="Hi there"
#
# change(String1)
#
# print(String1)


####################
def simple_interest(p,t,r):
    return (p*t*r)/100
print("Simple Interest: ",simple_interest(10,t=10,r=1900))
