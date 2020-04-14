from selenium import webdriver

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

# В метод execute_script мы передали текст js-скрипта и найденный элемент button, к которому нужно будет проскролить
# страницу. После выполнения кода элемент button должен оказаться в верхней части страницы.

# Также можно проскролить всю страницу целиком на строго заданное количество пикселей.
# Эта команда проскроллит страницу на 100 пикселей вниз:
browser.execute_script("window.scrollBy(0, 100);")