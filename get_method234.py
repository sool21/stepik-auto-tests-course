from selenium import webdriver
import time
import os 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    time.sleep(1)
    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys(y)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    time.sleep(10)
    browser.quit()

