import unittest
from selenium.webdriver import Chrome
import HtmlTestRunner
class TestDemo(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = Chrome(executable_path="C:\Installables_Selenium\chromedriver_win32\chromedriver.exe")
        self.driver.get("https://google.com")
        self.driver.maximize_window()

    def test_SearchGoogle(self):
        print("Title of the web page is --->",self.driver.title)


    def test_SearchBing(self):
        print("Title of the web page is --->", self.driver.title)
        self.assertEqual("Google","google","Texts  are diffrent")

    @classmethod
    def tearDown(self):
        self.driver.close()

    @unittest.SkipTest#skip, skipIf(condition,message)
    def test_serachText(self):
        print("HIIIIIIII")

if __name__=="__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\\Users\\spattanayak5\\PycharmProjects\\Practice\\Reports\\"))
#setup class and teardown class method runs only once in a class
#Assertion