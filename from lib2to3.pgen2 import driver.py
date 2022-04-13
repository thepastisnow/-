from cgitb import html
from dis import _HaveCodeOrStringType
from distutils.command import install
from lib2to3.pgen2 import driver
from multiprocessing import context
from os import WSTOPPED
from re import T
from tokenize import Double
from turtle import settiltangle
from xml.dom.minidom import Element
from xml.etree.ElementPath import xpath_tokenizer
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.baidu.com")
sleep(3)
context = driver.find_element(By.ID,'su')
ActionChains(driver).context_click(context).perform()
sleep(5)

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.baidu.com")
sleep(3)
driver.find_element(By.ID,'kw').send_keys("20381110733张蕴琛")
double = driver.find_element(By.ID,'su')
sleep(4)
ActionChains(driver).double_click().perform()

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.baidu.com")
sleep(2)
driver.find_element(By.ID,'kw').send_keys('哇嘎哇嘎嘿呀')

from selenium.webdriver.common.by import By
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.baidu.com")
driver.implicitly_wait(3)
driver.find_element(By.ID,'kw').send_keys('哇嘎哇嘎嘿呀')

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.baidu.com')
Element = WebDriverWait(driver,5,0,5).until(EC.presence_of_elements_located((By.ID,'kw')))
Element.send_keys("20381110733zyc")

from selenium import webdriver
import time as t
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("C:\\Users\\Administrator\\Documents\\HBuilderProjects\\HelloHBuilder\\123456789.html")
driver.switch_to.frame('iframeOne')
driver.find_element(By.NAME,"username").send_keys("zyc")
t.sleep(3)
driver.find_element(By.NAME,"password").send_keys("123456")
driver.switch_to.default_content()

from selenium import webdriver
import time as t
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("C:\\Users\\Administrator\\Documents\\HBuilderProjects\\HelloHBuilder\\123456789.html")
t.sleep(3)
driver.switch_to.frame('iframeOne')
driver.switch_to.frame('iframeTwo')
driver.find_element(By.NAME,"username").send_keys("zyc")
t.sleep(3)
driver.find_element(By.NAME,"password").send_keys("123456")
driver.switch_to.default_content()

import imp
from lib2to3.pgen2 import driver
from selenium import webdriver
import time as t
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("C:\\Users\\Administrator\\Documents\\HBuilderProjects\\HelloHBuilder\\123456789.html")
t.sleep(3)
driver.switch_to.frame('iframeOne')
driver.switch_to.default_content()
driver.switch_to.frame('iframeTwo')
driver.find_element(By.NAME,"username").send_keys("zyc")
t.sleep(4)
driver.find_element(By.name,"password").send_keys("123456789")

from selenium import webdriver
import time as t
from selenium.webdriver.common.by import By 
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("C:\\Users\\Administrator\\Documents\\HBuilderProjects\\HelloHBuilder\\fromSwitch.html")
t.sleep(2)
xpath_iframe=driver.find_element(By.XPATH,"div[@id='webTest']/div/iframe")
driver.switch_to.frame(xpath_iframe)
driver.find_element(By.NAME,"username").send_keys("zyc")
t.sleep(4)
driver.find_element(By.NAME,"password").send_keys("123456789")
driver.switch_to.default_content()

from selenium import webdriver
import time as t
from selenium.webdriver.common.by import By 
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.baidu.com/")
driver.find_elements(By.CLASS_NAME,"mnav")[3].click()
t.sleep(3)
driver.switch_to.window(driver.window_handles[1])
driver.find_element(By.ID,"wd1").send_keys("zyc")
driver.find_elements(By.CLASS_NAME,"search_btn")[0].click()

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By 
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.baidu.com/")
t.sleep(3)
driver.find_elements(By.CLASS_NAME,"mnav")[3].click()
windows=driver.window_handles
sleep(3)
driver.switch_to.window(windows[0])
sleep(3)
driver.switch_to.window(windows[1])
sleep(3)
driver.find_element(By.ID,"wd1").send_keys("haha")
sleep(3)
driver.find_elements(By.CLASS_NAME,"search_btn")[0].click()
sleep(3)
driver.switch_to.window(windows[0])
sleep(3)
driver.find_element(By,id,"KW").s

from selenium  import webdriver 
from time import sleep
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.baidu.com/")
sleep(6)
driver.find_elements(By.CLASS_NAME,"mnav")[3].click()
sleep(2)
windows=driver.window_handles
sleep(6)
driver.switch_to.window(windows[0])
sleep(6)

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.baidu.com/")
setting=driver.find_element(By.ID,"s-usersetting-top")
ActionChains(driver).move_to_element(setting).perform()
sleep(6)
driver.find_element(By.LINK_TEXT,"搜索设置").click()
sleep(6)
driver.find_element(By.ID,"SL_2").click()
sleep(6)
driver.find_element(By.ID,"nr_2").click()
sleep(6)
driver.find_elements(By.CLASS_NAME,"prefpanelgo")[0].click()
alert_text=driver.switch_to.alert.text
print(alert_text)

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.baidu.com/")
setting=driver.find_element(By.ID,"s-usersetting-top")
ActionChains(driver).move_to_element(setting).perform()
sleep(6)
driver.find_element(By.LINK_TEXT,"搜索设置").click()
sleep(6)
driver.find_element(By.ID,"SL_2").click()
sleep(6)
driver.find_element(By.ID,"nr_2").click()
sleep(2)
driver.find_elements(By.CLASS_NAME,"prefpanelgo")[0].click()
sleep(6)
driver.switch_to.alert.accept()
sleep(6)
driver.find_element(By.ID,"kw").send_keys("zyc")
driver.find_element(By.ID,"su").click()

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.baidu.com/")
setting=driver.find_element(By.ID,"s-usersetting-top")
ActionChains(driver).move_to_element(setting).perform()
sleep(6)
driver.find_element(By.LINK_TEXT,"搜索设置").click()
sleep(6)
driver.find_element(By.CLASS_NAME,"prefpanelresore").click()
sleep(6)
driver.switch_to.alert.dismiss()
sleep(6)
driver.find_element(By.ID,"kw").send_keys("zyc")
driver.find_element(By.ID,"su").click()
