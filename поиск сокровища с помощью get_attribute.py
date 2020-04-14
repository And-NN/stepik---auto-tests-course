from selenium import webdriver
import math
import time
link = "http://suninjuly.github.io/get_attribute.html"


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    #sunduk = browser.find_element_by_id("treasure")
    sunduk = browser.find_element_by_css_selector("img#treasure")
    x_element = sunduk.get_attribute("valuex")
    x = int(x_element)
    y = calc(x)
    input = browser.find_element_by_id("answer")
    input.send_keys(y)

    # Ищем чекбокс I'm the robot
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()

    # Выбираем радиокнопку Robots rule
    option2 = browser.find_element_by_id("robotsRule")
    option2.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
