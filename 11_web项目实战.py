import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://sellshop.5istudy.online/sell/user/login_page")

# 输入账户
driver.find_element(By.ID,"username").send_keys("test13")
# 输入密码
driver.find_element(By.ID,"password").send_keys("123456")
# 点击登录
driver.find_element(By.XPATH,"//p[@class='login button']/input").click()
# 点击新增
driver.find_element(By.CSS_SELECTOR,'a[href="/sell/seller/product/index"]').click()
# 新增内容
driver.find_element(By.NAME,"productName").send_keys('中华香烟')
driver.find_element(By.NAME,"productPrice").send_keys('45')
driver.find_element(By.NAME,"productStock").send_keys('999')
driver.find_element(By.NAME,"productDescription").send_keys('好东西')
driver.find_element(By.NAME,"productIcon").send_keys('https://img2.baidu.com/it/u=2135313359,4098486892&fm=253&fmt=auto&app=138&f=JPEG?w=749&h=500')
select = Select(driver.find_element(By.NAME,'categoryType'))
select.select_by_value("55")
driver.find_element(By.XPATH,'//button[@class="btn btn-default"]').click()
time.sleep(3)
driver.close()
