from selenium import webdriver
from time import sleep
# 指定浏览器的操作驱动
driver = webdriver.Chrome(R"D:\chromedriver\chromedriver.exe")
# 获取网址
driver.get("http://www.baidu.com")
# 找到页面的标签,并填入key 按Id找
# driver.find_element_by_id("kw").send_keys("hahah")

#按name找
# driver.find_element_by_name("wd").send_keys("hahah")

# 按classname找
# driver.find_element_by_class_name("s_ipt").send_keys("hahah")

# 按xpath找
driver.find_element_by_xpath("//input[@id='kw']").send_keys("hahha")
sleep(3)
driver.quit()