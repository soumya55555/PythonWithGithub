import unittest

class LoginTest(unittest.TestCase):
    def test_LoginByFB(self):
        print("Login using  FB")
    def test_LoginByGmail(self):
        print("Login using  Gmail")
    def test_LoginByPnone(self):
        print("Login using  Phone")

if __name__=="__main__":
    unittest.main()