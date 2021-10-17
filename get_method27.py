from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_tag_name("img")
    x_attribute = x_element.get_attribute("valuex")
    print (x_attribute)
    print(x_attribute)
    y = calc(x_attribute)
    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys(y)
    checkbox = browser.find_element_by_css_selector("#robotCheckbox")
    checkbox.click()    
    radiobutton = browser.find_element_by_css_selector("#robotsRule")
    radiobutton.click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    time.sleep(10)
    browser.quit()

