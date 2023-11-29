from selenium import webdriver

# 打开目标网页
driver = webdriver.Chrome()
driver.get("http://www.lagou.com")
print(driver.title)

# 找到页面中的x,并点击它。
driver.find_element()