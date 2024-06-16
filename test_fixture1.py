# from selenium import webdriver
# from selenium.webdriver.common.by import By
# link = "http://selenium1py.pythonanywhere.com/"
#
#
# class TestMainPage1():
#
#     @classmethod
#     def setup_class(self):
#         print("\nstart browser for test suite..")
#         self.browser = webdriver.ChromiumEdge()
#
#     @classmethod
#     def teardown_class(self):
#         print("quit browser for test suite..")
#         self.browser.quit()
#
#     def test_guest_should_see_login_link(self):
#         self.browser.get(link)
#         self.browser.find_element(By.CSS_SELECTOR, "#login_link")
#
#     def test_guest_should_see_basket_link_on_the_main_page(self):
#         self.browser.get(link)
#         self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
#
#
# class TestMainPage2():
#
#     def setup_method(self):
#         print("start browser for test..")
#         self.browser = webdriver.ChromiumEdge()
#
#     def teardown_method(self):
#         print("quit browser for test..")
#         self.browser.quit()
#
#     def test_guest_should_see_login_link(self):
#         self.browser.get(link)
#         self.browser.find_element(By.CSS_SELECTOR, "#login_link")
#
#     def test_guest_should_see_basket_link_on_the_main_page(self):
#         self.browser.get(link)
#         self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# link = "http://selenium1py.pythonanywhere.com/"
#
#
# @pytest.fixture(scope="class")
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.ChromiumEdge()
#     yield browser
#     print("\nquit browser..")
#     browser.quit()


# class TestMainPage1():
#
#     # вызываем фикстуру в тесте, передав ее как параметр
#     @pytest.mark.smoke
#     def test_guest_should_see_login_link(self, browser):
#         print("start test1")
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, "#login_link")
#         print("finish test1")
#
#     def test_guest_should_see_basket_link_on_the_main_page(self, browser):
#         print("start test2")
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
#         print("finish test2")

import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.ChromiumEdge()
    yield browser
    print("\nquit browser..")
    browser.quit()

class TestMainPage():
    # номер 1
    @pytest.mark.xfail
    @pytest.mark.smoke
    def test_guest_can_login(self, browser):
        assert True

    # номер 2
    @pytest.mark.regression
    def test_guest_can_add_book_from_catalog_to_basket(self, browser):
        assert True

class TestBasket():
    # номер 3
    @pytest.mark.skip(reason="not implemented yet")
    @pytest.mark.smoke
    def test_guest_can_go_to_payment_page(self, browser):
        assert True

    # номер 4
    @pytest.mark.smoke
    def test_guest_can_see_total_price(self, browser):
        assert True

@pytest.mark.skip
class TestBookPage():
    # номер 5
    @pytest.mark.smoke
    def test_guest_can_add_book_to_basket(self, browser):
        assert True

    # номер 6
    @pytest.mark.regression
    def test_guest_can_see_book_price(self, browser):
        assert True

# номер 7
@pytest.mark.beta_users
@pytest.mark.smoke
def test_guest_can_open_gadget_catalogue(browser):
    assert True
