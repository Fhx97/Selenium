# selenium可以自动打开浏览器
# 输入网址
# 能从页面里提取东西
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 创建Chrome浏览器的WebDriver对象,变量实例化
driver = webdriver.Chrome()

# 使用WebDrive对象打开指定网址
driver.get("https://www.bilibili.com/")


# 找到输入框的位置，输入'丰小帅'
driver.find_element(By.CLASS_NAME,'nav-search-input').send_keys('丰小帅')
# # 找到搜索框位置，点击搜索
driver.find_element(By.CLASS_NAME,'nav-search-btn').click()

time.sleep(5)
# # 获取网页的title标签
# print(driver.title)
# # 关闭浏览器
driver.quit()