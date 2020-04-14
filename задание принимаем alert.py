from selenium import webdriver
import math
import time

def myFunc(x):
    return math.log(abs(12 * math.sin(x)))


link = "http://suninjuly.github.io/alert_accept.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_tag_name("button")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    text_x = browser.find_element_by_id("input_value")  # находим число
    x = int(text_x.text)
    y = myFunc(x)  # подставляем x в формулу

    # вставляем ответ в поле ввода
    input = browser.find_element_by_id("answer")
    input.send_keys(str(y))

    # Отправляем заполненную форму
    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
