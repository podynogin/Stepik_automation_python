from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get("http://suninjuly.github.io/explicit_wait2.html")

try:

    price = WebDriverWait(browser, 60).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button = browser.find_element_by_id("book")
    button.click()
    # капча
    browser.implicitly_wait(1)
    x_element = browser.find_element_by_tag_name(".nowrap#input_value")
    x = x_element.text
    y = calc(x)
    x_input = browser.find_element_by_tag_name(".form-control")
    x_input.send_keys(y)
    submit = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID,"solve"))
    )
    submit.click()

finally:
    time.sleep(10)
    browser.quit()