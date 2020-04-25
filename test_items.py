import time


def test_add_to_basket(browser):
    browser.implicitly_wait(5)
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    #time.sleep(30)
    add_button = browser.find_element_by_xpath("//*[@id='add_to_basket_form']/button")
    assert add_button, 'Button "Add to basket not found"'
    add_button.click()
    time.sleep(5)

