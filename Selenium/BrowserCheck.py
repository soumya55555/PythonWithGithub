from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome(executable_path="C:\Installables_Selenium\chromedriver_win32\chromedriver.exe")
driver.get("https://www.google.com")
driver.implicitly_wait(1000)
driver.maximize_window()
title_of_page=driver.title
print("title of the page is ", title_of_page)
driver.close()