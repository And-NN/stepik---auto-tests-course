'''
Для хранения часто употребимых фикстур и хранения глобальных настроек нужно использовать файл conftest.py,
который должен лежать в директории верхнего уровня в вашем проекте с тестами. Можно создавать дополнительные файлы
conftest.py в других директориях, но тогда настройки в этих файлах будут применяться только к тестам в под-директориях.
'''

import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    print("\nStart browser for test...")
    browser = webdriver.Chrome()
    yield browser
    print("\nQuit browser...")
    browser.quit()

