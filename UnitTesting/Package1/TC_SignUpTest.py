import unittest
class SignUpTest(unittest.TestCase):
    def test_signUpByFB(self):
        print("Sign up using FB")

    def test_signUpByGmail(self):
        print("Sign up using Gmail")
    def test_signUpByPhnone(self):
        print("Sign up using Phone")

if __name__=="__main__":
    unittest.main()