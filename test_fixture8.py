'''
Чтобы не было предупреждений Unknown pytest.mark.smoke - is this a typo?  You can reg
ister custom marks to avoid this warning
Нужно создать файл pytest.ini и добавить в него
[pytest]
markers =
    smoke: blokers test which must started immediately after commit
    regression: kit of regression tests before release
Чтобы запустить тест с нужной маркировкой, нужно передать в командной строке параметр -m и нужную метку:
pytest -s -v -m smoke test_fixture8.py
'''

import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nStart browser for test...")
    browser = webdriver.Chrome()
    yield browser
    print("\nQuit browser...")
    browser.quit()


class TestMainPage1():

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")


'''
Инверсия
Чтобы запустить все тесты, не имеющие заданную маркировку, можно использовать инверсию. Для запуска всех тестов, не отмеченных как smoke, нужно выполнить команду:

pytest -s -v -m "not smoke" test_fixture8.py


Объединение тестов с разными маркировками
Для запуска тестов с разными метками можно использовать логическое ИЛИ. Запустим smoke и regression-тесты:

pytest -s -v -m "smoke or regression" test_fixture8.py
'''