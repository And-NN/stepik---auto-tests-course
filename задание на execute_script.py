from selenium import webdriver
from selenium.webdriver.support.ui import Select

import math
import time

link = "http://SunInJuly.github.io/execute_script.html"


def myFunc(x):
    return math.log(abs(12 * math.sin(x)))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    text_x = browser.find_element_by_id("input_value")  # находим первое число
    x = int(text_x.text)

    y = myFunc(x)  # подставляем x в формулу

    # вставляем ответ в поле ввода
    input = browser.find_element_by_id("answer")
    input.send_keys(str(y))

    # Ищем чекбокс I'm the robot
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()

    # Скролим страницу, чтобы драйвер увидел кнопку отправки из под футера
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    # Выбираем радиокнопку Robots rule
    option2 = browser.find_element_by_id("robotsRule")
    option2.click()
    # Отправляем заполненную форму
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
