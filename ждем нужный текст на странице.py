from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 12 секунд, пока не появится нужная цена
price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
button = browser.find_element_by_id("book")
button.click()

num = browser.find_element_by_id("input_value")
num = num.text
x = int(num)
y = calc(x)
input = browser.find_element_by_id("answer")
input.send_keys(y)
button = browser.find_element_by_id("solve")
button.click()
