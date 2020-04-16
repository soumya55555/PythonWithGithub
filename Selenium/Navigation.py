from selenium import webdriver

from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome(executable_path="C:\Installables_Selenium\chromedriver_win32\chromedriver.exe")
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(1000)
(driver.title)
driver.maximize_window()
driver.find_element_by_xpath("//button[text()='Open Window']").click()
print(driver.title)
#driver.back()



