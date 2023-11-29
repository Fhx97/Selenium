import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# 窗口最大化
driver.maximize_window()

# driver.get('http://www.baidu.com')
# # 通过id定位，By.ID在HTML中是唯一的，因此可以使用id定位确保找到页面上的唯一元素。
# driver.find_element(By.ID,"kw").send_keys("丰小帅")
# driver.find_element(By.ID,'su').click()
# time.sleep(3)
# # driver.quit()


# driver.get("https://www.bilibili.com/")
# driver.find_elements(By.CLASS_NAME,'channel-link')[5].click()
# time.sleep(3)

# # 标签定位不常用
# driver.get("https://www.bilibili.com/")
# driver.find_element(By.TAG_NAME,"input").send_keys("丰小帅")
# time.sleep(3)

# driver.get("http://www.baidu.com/")
# driver.find_elements(By.LINK_TEXT,"新闻")[0].click()
# time.sleep(3)

# # 包含关系(可点击链接标签)
# driver.get("http://www.baidu.com/")
# driver.find_elements(By.PARTIAL_LINK_TEXT,"新闻")[0].click()
# time.sleep(3)

# # 根据id定位别忘了#
# driver.get("http://www.baidu.com/")
# driver.find_element(By.CSS_SELECTOR,"#kw").send_keys("丰小帅")
# driver.find_element(By.CSS_SELECTOR,"#su").click()
# time.sleep(3)
# driver.close()
# driver.quit()

# # 根据class属性值定位
# driver.get("https://www.bilibili.com/")
# driver.find_element(By.CSS_SELECTOR,".nav-search-input").send_keys("丰小帅")
# time.sleep(3)

# # 根据name属性定位
# driver.get("http://www.baidu.com/")
# driver.find_element(By.CSS_SELECTOR,"[name='wd']").send_keys("丰小帅")
# driver.find_element(By.CSS_SELECTOR,"#su").click()
# time.sleep(3)
# driver.close()

# # 根据标签属性定位
# driver.get("http://www.baidu.com/")
# # driver.find_element(By.CSS_SELECTOR,"a[href='http://image.baidu.com/']").click()
# # 模糊匹配-包含
# # driver.find_element(By.CSS_SELECTOR,"a[href*='image.baidu']").click()
# # 模糊匹配-匹配开头
# # driver.find_element(By.CSS_SELECTOR,"a[href^='http://image']").click()
# # 模糊匹配-匹配结尾
# driver.find_element(By.CSS_SELECTOR,"a[href$='image.baidu.com/']").click()
# time.sleep(3)
# driver.close()

# # 组合定位
# driver.get("http://www.baidu.com/")
# driver.find_element(By.CSS_SELECTOR,"input.s_ipt").send_keys("丰小帅")
# time.sleep(3)
# driver.close()

# # # 定位子元素
# driver.get("http://www.baidu.com/")
# # # driver.find_element(By.CSS_SELECTOR,"div#s-top-left>a").click()
# driver.find_element(By.CSS_SELECTOR,"div#s-top-left>a:first-child").click()
# # # driver.find_element(By.CSS_SELECTOR,"div.s-top-left-new.s-isindex-wrap>a").click()
# # # driver.find_elements(By.CSS_SELECTOR,"div.s-top-left-new.s-isindex-wrap>a")[2].click()
# # driver.find_element(By.CSS_SELECTOR,"div.s-top-left-new.s-isindex-wrap>a:nth-child(3)").click()
# time.sleep(3)
# driver.close()

# xpath是一种在XML文档(可拓展标记语言，主要用于传输数据)中查找信息的语言。
# html文档的结果和标签遵循XML的基本规则，因此xpath可以有效用于在html文档中定位元素。
# # xpath绝对路径
# driver.get("http://www.baidu.com")
# driver.find_element(By.XPATH,"/html/body/div/div/div[3]/a[4]").click()
# time.sleep(3)
# driver.close()
# driver.quit()

# # xpath根据id和class定位
# driver.get("http://www.baidu.com")
# # driver.find_element(By.XPATH,"//input[@id='kw']").send_keys("丰小帅")
# driver.find_element(By.XPATH,"//input[@class='s_ipt']").send_keys("丰小帅")
# time.sleep(3)
# driver.close()

# # 多个属性组合定位
# driver.get("http://www.baidu.com")
# driver.find_element(By.XPATH,"//input[@class='s_ipt' and @id='kw']").send_keys("丰小帅")
# time.sleep(3)
# driver.close()

# # 对多组数据进行下标定位
# driver.get("http://www.baidu.com")
# driver.find_element(By.XPATH,"//div[@id='s-top-left']/a[4]").click()
# time.sleep(3)
# driver.close()

# # 文本等于
# driver.get("http://www.baidu.com")
# driver.find_element(By.XPATH,"//span[text()='为中国式现代化营造有利法治条件']").click()
# time.sleep(3)
# driver.close()

# # 文本包含
# driver.get("http://www.baidu.com")
# driver.find_element(By.XPATH,"//span[contains(text(),'阿姨')]").click()
# time.sleep(3)
# driver.close()

# 同级定位
driver.get("http://www.baidu.com")
# 下一级
# driver.find_element(By.XPATH,"//a[contains(text(),'贴吧') and @class = 'mnav c-font-normal c-color-t']/following-sibling::a[2]").click()
# 上一级
driver.find_element(By.XPATH,"//a[contains(text(),'贴吧') and @class = 'mnav c-font-normal c-color-t']/preceding-sibling::a[2]").click()
time.sleep(3)
driver.close()