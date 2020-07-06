from selenium import webdriver
#from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

'''设置浏览器属性'''
# chrome_opt = Options()
# chrome_opt.add_argument('--windows-size=500,500')
# chrome_opt.add_experimental_option("add_experimental_option")

# driver = webdriver.Chrome(chrome_options=chrome_opt)  # 启动浏览器
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
time.sleep(3)

driver.find_element_by_xpath(".//*[@id='hotsearch-content-wrapper']/li[1]/a/span[2]").click()
time.sleep(5)

"""
# driver .find_element_by_id("kw").send_keys("武汉")
# driver.find_element(By.ID,"kw").send_keys("武汉")
driver.find_element("id", "kw").send_keys("武汉")
time.sleep(2)

driver .find_element_by_id("kw").clear()
time.sleep(2)

driver .find_element_by_id("kw").send_keys("新冠疫情")
time.sleep(2)

driver .find_element_by_id("su").click()
time.sleep(4)
"""
driver.close()


