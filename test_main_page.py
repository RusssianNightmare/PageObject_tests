import pytest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def test_guest_can_go_to_login_page(browser):
    # Открываем страницу
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    
    # Проверяем, что ссылка на логин существует
    try:
        login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()
    except NoSuchElementException:
        pytest.fail("Ссылка на логин не найдена на главной странице")
    
    # Проверяем, что мы действительно попали на страницу логина
    try:
        # Ждём появления характерного элемента страницы логина
        browser.find_element(By.CSS_SELECTOR, "#login_form")
        print("✅ Успешно перешли на страницу логина")
    except NoSuchElementException:
        pytest.fail("Не удалось перейти на страницу логина")
