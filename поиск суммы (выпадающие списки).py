from selenium import webdriver
from selenium.webdriver.support.ui import Select

import time
link = "http://suninjuly.github.io/selects1.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_id("num1")  # находим первое число
    num1 = int(num1.text)
    num2 = browser.find_element_by_id("num2")  # находим второе число
    num2 = int(num2.text)

    summ = num1 + num2  # вычисляем сумму

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(summ))  # ищем элемент с текстом суммы

    # Отправляем заполненную форму
    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
