from selenium import webdriver
import time

driver = webdriver.Chrome()  #启动浏览器

driver.get("https://test.lptiyu.com/run/index.php/Index/login.html")
time.sleep(3)

driver.find_element_by_id("email").send_keys("admin_zym")
driver.find_element_by_id("password").send_keys("Lepao123..")
time.sleep(2)
driver.find_element_by_id("btn_login").click()
