import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()

# # alert弹框
# driver.get("https://sahitest.com/demo/alertTest.htm")
# driver.find_element(By.NAME,'b1').click()
# # 固定用法，使用alert.text获取弹框的文字
# print(driver.switch_to.alert.text)
# # 点击确定
# driver.switch_to.alert.accept()
# time.sleep(3)
# driver.close()

# # confirm弹窗
# driver.get("https://sahitest.com/demo/confirmTest.htm")
# driver.find_element(By.NAME,'b1').click()
# # 固定用法，使用alert.text获取弹框的文字
# print(driver.switch_to.alert.text)
# # # 点击确定
# # driver.switch_to.alert.accept()
# # 点击取消
# driver.switch_to.alert.dismiss()
# time.sleep(3)
# driver.close()

# prompt输入框
driver.get("https://sahitest.com/demo/promptTest.htm")
driver.find_element(By.NAME,'b1').click()
driver.switch_to.alert.send_keys("丰小帅！！！")
# 点击确定
driver.switch_to.alert.accept()
# # 点击取消
# driver.switch_to.alert.dismiss()
time.sleep(3)
driver.close()