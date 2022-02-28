
#from https://www.youtube.com/watch?v=2jySmTleWF4
from selenium import webdriver
from getpass import getpass



driver = webdriver.Chrome("C:\\Users\\akothapa\\PycharmProjects\\webdriver\\chromedriver.exe")
driver.get("https://facebook.com")

driver.find_element_by_name("email").send_keys("arjun98854")
driver.find_element_by_name("pass").send_keys("Fiat123!")
driver.find_element_by_name("login").click()

