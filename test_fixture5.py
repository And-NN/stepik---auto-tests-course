'''
Для фикстур можно задавать область покрытия фикстур. Допустимые значения:
function - фикстура будет вызываться один раз для тестового метода
class - фикстура будет вызываться один раз для класса
module - фикстура будет вызываться один раз для модуля
session - фикстура будет вызываться один раз для всех тестов, запущенных в данной сессии
'''

import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="class")  # теперь браузер запустится только один раз для всего класса и две функции выполнятся в одном окне браузера
def browser():
    print("\nStart browser for test...")
    browser = webdriver.Chrome()
    yield browser
    print("\nQuit browser...")
    browser.quit()


class TestMainPage1():
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser):
        print("start test1")
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")
        print("finish test1")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        print("start test2")
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")
        print("finish test2")
