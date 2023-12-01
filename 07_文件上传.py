import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://sahitest.com/demo/php/fileUpload.htm")
# 获取input文件上传元素
upload = driver.find_element(By.ID,'file')
upload.send_keys(r'D:\Fhx图片\电脑壁纸啊\F5.jpg')
driver.find_elements(By.NAME,'submit')[0].click()


time.sleep(3)
driver.close()
