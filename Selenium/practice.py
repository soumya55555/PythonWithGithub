import logging
logging.basicConfig(filename="test.log",
                    format='%(asctime)s: %(levelname)s: %(message)s')
# from selenium.webdriver import Chrome
# driver=Chrome(executable_path="C:\Installables_Selenium\chromedriver_win32\chromedriver.exe")
# driver.get("http://newtours.demoaut.com/")
# driver.maximize_window()
# driver.implicitly_wait(1000)
# driver.find_element_by_name("userName").send_keys("mercury")
# driver.find_element_by_name("password").send_keys("mercury")
# driver.find_element_by_name("login").click()
# driver.save_screenshot("C:/Users/spattanayak5/PycharmProjects/Practice/Selenium/screenshots/mercury.png")
###working with log##########
#debug,info,erro

logger=logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.info("This is a info msg")
logger.debug("This is Debug msg")
logger.warning("this ia a warning msg")
logger.error("This is a error msg")
logger.critical("This ia a critical log msg")


