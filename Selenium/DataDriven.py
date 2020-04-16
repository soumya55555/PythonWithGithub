from Selenium import Xl_Utility
from selenium.webdriver import Chrome
driver=Chrome(executable_path="C:\Installables_Selenium\chromedriver_win32\chromedriver.exe")
driver.get("http://newtours.demoaut.com/")
driver.maximize_window()
driver.implicitly_wait(1000)
path="C:\Soumya\data.xlsx"
rows=Xl_Utility.getRow_count(path,"Sheet1")
for r in range(2,rows+1):
    userName=Xl_Utility.read_data(path,"Sheet1",r,colnum=1)
    password = Xl_Utility.read_data(path, "Sheet1", r,colnum=2)

    driver.find_element_by_name("userName").send_keys(userName)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_name("login").click()



    if driver.title=="Find a Flight: Mercury Tours:":
        print("test is passed")
        Xl_Utility.write_data(path,"Sheet1",r,3,"Passed")
    else:
        print("test is failed")
        Xl_Utility.write_data(path, "Sheet1", r, 3, "Failed")
    driver.close()