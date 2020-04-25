'''
Теперь добавим в наш тестовый класс тест, который проверяет наличие кнопки "Избранное":

def test_guest_should_see_search_button_on_the_main_page(self, browser):
     browser.get(link)
     browser.find_element_by_css_selector("button.favorite")
Предположим, что такая кнопка должна быть, но из-за изменений в коде она пропала.
Пока разработчики исправляют баг, мы хотим, чтобы результат прогона ﻿всех ﻿наших тестов был успешен, но падающий тест
помечался соответствующим образом, чтобы про него не забыть. Добавим маркировку @pytest.mark.xfail для падающего теста.

pytest -rX -v test_fixture10.py
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

    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")

    @pytest.mark.xfail(reason="We are waiting for the addition of a button from developers")
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        browser.get(link)
        # Поменяем селектор в последнем тесте, чтобы тест начал проходить
        browser.find_element_by_css_selector("button.favorite")
        # browser.find_element_by_css_selector("input.btn.btn-default")

'''
Когда баг починят, мы это узнаем, ﻿﻿так как теперь тест будет отмечен как XPASS (“unexpectedly passing” - 
неожиданно проходит). После этого маркировку xfail для теста можно удалить. Кстати, к маркировке xfail можно 
добавлять параметр reason. Чтобы увидеть это сообщение в консоли, при запуске нужно добавлять параметр pytest -rx.

документаци: https://docs.pytest.org/en/latest/skipping.html#xfail-mark-test-functions-as-expected-to-fail
'''