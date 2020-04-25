from selenium import webdriver
import time
import unittest

browser = webdriver.Chrome()

class TestReg(unittest.TestCase):
    def test_reg1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser.get(link)

        input1 = browser.find_element_by_css_selector(".first_block input.form-control.first")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector(".first_block input.form-control.second")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector(".first_block input.form-control.third")
        input3.send_keys("root@nic.ru")
        input4 = browser.find_element_by_css_selector(".second_block input.form-control.first")
        input4.send_keys("+79200148500")
        input4 = browser.find_element_by_css_selector(".second_block input.form-control.second")
        input4.send_keys("Timiryazeva str, 7/2")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()


    def test_reg2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser.get(link)

        input1 = browser.find_element_by_css_selector(".first_block input.form-control.first")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector(".first_block input.form-control.second")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector(".first_block input.form-control.third")
        input3.send_keys("root@nic.ru")
        input4 = browser.find_element_by_css_selector(".second_block input.form-control.first")
        input4.send_keys("+79200148500")
        input4 = browser.find_element_by_css_selector(".second_block input.form-control.second")
        input4.send_keys("Timiryazeva str, 7/2")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()


if __name__ == "__main__":
    unittest.main()

