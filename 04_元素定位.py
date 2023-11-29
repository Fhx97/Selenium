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

