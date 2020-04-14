from selenium import webdriver
import time
import os

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")

    # опять заполняем форму
    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("root@kis.ru")

    # находим кнопку загрузки файла
    element = browser.find_element_by_id("file")
    # получаем путь к директории
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # сливаем ауть с именем файла
    file_path = os.path.join(current_dir, 'file.txt')
    # выбираем файл
    element.send_keys(file_path)
    # жмём отправить
    button = browser.find_element_by_tag_name("button")
    button.click()
finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
