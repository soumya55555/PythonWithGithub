from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome(executable_path="C:\Installables_Selenium\chromedriver_win32\chromedriver.exe")
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(1000)
driver.maximize_window()
# elm=driver.find_elements_by_xpath("//label/input[@name='radioButton']")
# print(type(elm))
# for radio in elm:
#     radio.click()
#     time.sleep(100)


# wait=WebDriverWait(driver,100)
# # element=wait.until(EC.alert_is_present())
# elm=driver.find_element_by_xpath("//select[@id='dropdown-class-example']")
# select class
# sel=Select(elm)
# sel.select_by_index(1)
# lst_options=sel.options
# for option in lst_options:
#     print(option.text)

# links=driver.find_elements_by_tag_name("a")
# for link in links:
#     print(link.text)

#working with alert
# driver.find_element_by_id("alertbtn").click()
# driver.switch_to.alert.accept()
# driver.find_element_by_id("confirmbtn").click()
# time.sleep(10)
# driver.switch_to.alert.dismiss()

#working with browsers
#current window handle and WINDOW HANDLES
# driver.find_element_by_id("opentab").click()
# print(driver.current_window_handle)
# windows=driver.window_handles
# for window in windows:
#     driver.switch_to.window(window)
#     print(driver.title)
#     driver.switch_to.default_content()
#
# driver.close()


#working with tables
# rows=driver.find_elements_by_xpath("//table/tbody/tr")
# data_column=driver.find_elements_by_xpath("//table/tbody/tr/td")
# for row in rows:
#     for data in data_column:
#         print(data.text)

#working with javascript
#driver.execute_script("window.scrollBy(0,500)")
elm=driver.find_element_by_xpath("//button[text()='Mouse Hover']")
driver.execute_script("arguments[0].scrollIntoView();",elm)
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
act=ActionChains(driver)
elm_mouse=driver.find_element_by_id("mousehover")
act.move_to_element(elm_mouse).perform()
