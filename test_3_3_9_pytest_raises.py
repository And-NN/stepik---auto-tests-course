import pytest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


# В первом тесте элемент будет найден, поэтому ошибка NoSuchElementException, которую ожидает контекстный менеджер
# pytest.raises, не возникнет, и тест упадёт.
def test_exception1():
    try:
        browser = webdriver.Chrome()
        browser.get("http://selenium1py.pythonanywhere.com/")
        with pytest.raises(NoSuchElementException):
            browser.find_element_by_css_selector("button.btn")
            pytest.fail("Не должно быть кнопки Отправить")
    finally: 
        browser.quit()


# Во втором тесте, как мы и ожидали, кнопка не будет найдена, и тест пройдет.
def test_exception2():
    try:
        browser = webdriver.Chrome()
        browser.get("http://selenium1py.pythonanywhere.com/")
        with pytest.raises(NoSuchElementException):
            browser.find_element_by_css_selector("no_such_button.btn")
            pytest.fail("Не должно быть кнопки Отправить")
    finally: 
        browser.quit()
