import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()

# radio
# driver.get("https://iviewui.com/view-ui-plus/component/form/radio")
# driver.find_elements(By.XPATH,'//input[@class="ivu-radio-input" and @type="radio"][1]').click()
# driver.find_elements(By.XPATH,'//input[@class="ivu-radio-input" and @type="radio"][2]').click()
# driver.find_elements(By.XPATH,'//input[@class="ivu-radio-input" and @type="radio"][3]').click()
# driver.find_elements(By.XPATH,"//span[text()='Apple']").click()

# # checkbox
# driver.get("https://iviewui.com/view-ui-plus/component/form/checkbox")
# driver.find_element(By.XPATH,'//span[text()="香蕉"]').click()
# time.sleep(3)
# driver.find_element(By.XPATH,"//span[text()='苹果']").click()
# time.sleep(3)
# driver.find_element(By.XPATH,"//span[text()='西瓜']").click()
# time.sleep(3)
# driver.close()
# driver.quit()

# # select选择器
# driver.get("https://sahitest.com/demo/selectTest.htm")
# select = Select(driver.find_element(By.ID,'s1Id'))
# # 根据index下标获取，从0开始
# # select.select_by_index(0)
# # 根据option的value进行选择
# # select.select_by_value('o3')
# # 根据实际内容进行筛选
# select.select_by_visible_text('o2')
# time.sleep(3)
# driver.close()
# driver.quit()


# # Cascader级联选择
# driver.get("https://iviewui.com/view-ui-plus/component/form/cascader")
# driver.find_element(By.XPATH,"//input[@class = 'ivu-input ivu-input-default']").click()
# driver.find_element(By.XPATH,'//li[contains(text(),"北京")]').click()
# driver.find_element(By.XPATH,'//li[contains(text(),"天坛")]').click()
# time.sleep(3)
# driver.close()


# TimePicker时间选择器
driver.get("https://iviewui.com/view-ui-plus/component/form/time-picker")
driver.find_element(By.XPATH,'//input[@class="ivu-input ivu-input-default ivu-input-with-suffix"]').send_keys('08:30:12')
driver.find_elements(By.XPATH,'//input[@class="ivu-input ivu-input-default ivu-input-with-suffix"]')[1].send_keys('08:30:12-20:38:24')
time.sleep(3)
driver.close()