# frame是网页开发中常见应用。例如页面布局、局部刷新、页面切割，都是frame的用途表现，使用frame会给用户带来非常舒适的使用感受。
# frame包括：frameset标签、frame标签、iframe标签。
# frameset和frame结合一起使用，可以对页面进行分割。例如sahitest的Frames Test对页面进行上下切割，并嵌套html页面。
# iframe是个内联框架，是在页面里生成个内部框架。可以嵌套多个html页面。大多网页使用的都是iframe框架，例如163邮箱。

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
# driver.get("https://sahitest.com/demo/iframesTest.htm")
#
# driver.find_element(By.ID,'checkRecord').clear()
# driver.find_element(By.ID,'checkRecord').send_keys('丰小帅')
# time.sleep(3)
# # 进入指定iframe,用下标表示
# driver.switch_to.frame(0)
# # driver.find_element(By.CSS_SELECTOR,'a[href="linkTest.htm"]').click()
# driver.find_element(By.ID,'open-self').click()
# time.sleep(3)
# driver.close()

# 打开本地的html文件,前言要加'file://'
driver.get(r"C:\Users\丰浩翔\Desktop\selenium\iframe_demo.html")
time.sleep(3)
driver.find_element(By.ID,'checkRecord').clear()
driver.find_element(By.ID,'checkRecord').send_keys('丰小帅')
time.sleep(3)
# 进入指定iframe,用下标表示
driver.switch_to.frame("iframe_id")
# driver.find_element(By.CSS_SELECTOR,'a[href="linkTest.htm"]').click()
driver.find_element(By.XPATH,'//span[text()="番剧"]').click()
# 退出iframe,切换到上一级driver.switch_to.parent_frame()
# 切换到主界面 driver.switch_to.default_content()
time.sleep(3)
driver.close()

