import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# 设置文件下载保存路径
chrome_options = webdriver.ChromeOptions()
prefs = {"download.default_directory":r"C:\Users\丰浩翔\Desktop\百二秦关终属楚"}
chrome_options.add_experimental_option("prefs",prefs)

driver = webdriver.Chrome(chrome_options)
driver.maximize_window()
driver.get("https://registry.npmmirror.com/binary.html?path=chromedriver/")
time.sleep(3)
driver.find_element(By.XPATH,"/html/body/table/tbody/tr[156]/td[2]").click()
time.sleep(3)
driver.close()