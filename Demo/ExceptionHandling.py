# import logging
# logging.basicConfig(filename="Mylog.log",level="DEBUG")
# try:
#     logging.info("The code might have exception")
#     sum=10/0
#
# except ZeroDivisionError as ze:
#     print("exception caught",ze)
#     logging.warning("Code came across exception")
# except ArithmeticError as ar:
#     print("if caught ",ar.__context__)
# #else gets executed when there is no exception in code
# else:
#     print("********************")
# finally:
#     print("Finaly i am here to close the code")

class LessLimitException(Exception):
    def __init__(self,amount):
        self.amount=amount
    def withdraw(self):
        if self.amount>=500:
            print("you are welcome,please enter the amount to proceed with transaction")
        else:
            raise LessLimitException("Your current balnace is less than 500")

c=LessLimitException(200)
c.withdraw()


