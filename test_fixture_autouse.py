import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture
def browser():
    print("\nStart browser for test...")
    browser = webdriver.Chrome()
    yield browser
    print("\nQuit browser...")
    browser.quit()


'''
При описании фикстуры можно указать дополнительный параметр autouse=True, который укажет, 
что фикстуру нужно запустить для каждого теста даже без явного вызова: 
'''

@pytest.fixture(autouse=True)
def prepare_data():
    print()
    print("Preparing some critical data for every test")


class TestMainPage1():
    def test_guest_should_see_login_link(self, browser):
        # не передаём как параметр фикстуру prepare_data, но она все равно выполняется
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")
