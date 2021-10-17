from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

def calc(x,y):
  return str(int(x)+int(y))

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_id("num1")
    a = input1.text
    input2 = browser.find_element_by_id("num2")
    b = input2.text
    y = calc(a, b)
    print(y)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(y)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    time.sleep(10)
    browser.quit()

