import pytest
from playwright.sync_api import expect
import time
import math
from .pages.main_page import MainPage


def test_guest_can_go_to_login_page(page):
    link = "http://selenium1py.pythonanywhere.com/"
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page = MainPage(page, link)
    page.open()
    page.go_to_login_page()


def test_guest_should_see_login_link(page):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(page, link)
    page.open()
    page.should_be_login_link()


# @pytest.mark.parametrize("link", [
#     "https://stepik.org/lesson/236895/step/1",
#     "https://stepik.org/lesson/236896/step/1",
#     "https://stepik.org/lesson/236897/step/1",
#     "https://stepik.org/lesson/236898/step/1",
#     "https://stepik.org/lesson/236899/step/1",
#     "https://stepik.org/lesson/236903/step/1",
#     "https://stepik.org/lesson/236904/step/1",
#     "https://stepik.org/lesson/236905/step/1"
# ])
# def test_guest_should_see_login_link(page, link):
#     answer = math.log(int(time.time()))
#     page.goto(f"{link}", wait_until="domcontentloaded")
#     login_link = page.locator(".navbar__auth_login")
#     login_link.click()
#     page.get_by_placeholder("E-mail").fill("n-armstrong@mail.ru")
#     page.get_by_placeholder("Пароль").fill("ILOVEBJA93")
#     page.get_by_role("button", name="Войти").click()
#     page.wait_for_load_state("networkidle")
#     page.get_by_placeholder("Напишите ваш ответ здесь...").fill(f"{answer}")
#     submit = page.get_by_role("button", name="Отправить")
#     expect(submit).to_be_enabled()
#     submit.click()
#     time.sleep(3)
#     text = page.locator(".smart-hints__hint")
#     assert text.text_content() == 'Correct!'