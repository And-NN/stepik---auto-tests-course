# к задаче про инопланетян https://stepik.org/lesson/237240/step/3?unit=209628

import time
import math
import pytest
from selenium import webdriver

pages = [
    '236895',
    '236896',
    '236897',
    '236898',
    '236899',
    '236903',
    '236904',
    '236905'
]


class TestAliens():

    @classmethod
    def setup_class(cls):
        print("\nStart browser for test...")
        cls.browser = webdriver.Chrome()

    @classmethod
    def teardown_class(cls):
        print("\nQuit browser for test...")
        cls.browser.quit()


    @pytest.mark.parametrize("num_page", pages)
    def test_open_url(self, num_page):
        self.browser.implicitly_wait(15)
        link = f'https://stepik.org/lesson/{num_page}/step/1'
        self.browser.get(link)
        print(' Проверяемый link: %s' % link)
        input = self.browser.find_element_by_tag_name("textarea")
        answer = math.log(int(time.time()))
        input.send_keys(str(answer))
        button = self.browser.find_element_by_css_selector(".submit-submission")
        button.click()
        time.sleep(1)
        feedBack = self.browser.find_element_by_class_name("smart-hints__hint")
        expected_result = feedBack.text
        assert expected_result == 'Correct!', print('Кусочек послания: ', expected_result)

