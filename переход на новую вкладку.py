from selenium import webdriver
import math
import time

def myFunc(x):
    return math.log(abs(12 * math.sin(x)))


link = "http://suninjuly.github.io/redirect_accept.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    start_window = browser.window_handles[0]  # запишем на всякий случай стартовое окно
    button = browser.find_element_by_class_name("trollface")  # найдем вертящуюся кнопку по классу
    button.click()  # кликаем по ней

    new_window = browser.window_handles[1]  # записываем дескриптор нового окна
    browser.switch_to.window(new_window)  # переходим на новую вкладку

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
