# import pytest
# from selenium import webdriver
# import time
# import unittest
# from selenium.webdriver.common.by import By
# class TestAbs(unittest.TestCase):
#     def test_abs1(self):
#         link = "http://suninjuly.github.io/registration1.html"
#         browser = webdriver.ChromiumEdge()
#         browser.get(link)
#
#         # Ваш код, который заполняет обязательные поля
#         input1 = browser.find_element(by='xpath', value='/html/body/div/form/div[1]/div[1]/input')
#         input1.send_keys("Ivan")
#         input2 = browser.find_element(by='xpath', value='/html/body/div/form/div[1]/div[2]/input')
#         input2.send_keys("Petrov")
#         input3 = browser.find_element(by='xpath', value='/html/body/div/form/div[1]/div[3]/input')
#         input3.send_keys("kirillnnov97@gmail.com")
#         input4 = browser.find_element(by='xpath', value='/html/body/div/form/div[2]/div[1]/input')
#         input4.send_keys("+79991365314")
#         input5= browser.find_element(by='xpath', value='/html/body/div/form/div[2]/div[2]/input')
#         input5.send_keys("Pochainskaya st.")
#         # Отправляем заполненную форму
#         button = browser.find_element(by='xpath', value='/html/body/div/form/button')
#         button.click()
#
#         # Проверяем, что смогли зарегистрироваться
#         # ждем загрузки страницы
#         time.sleep(1)
#
#         # находим элемент, содержащий текст
#         welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
#         # записываем в переменную welcome_text текст из элемента welcome_text_elt
#         welcome_text = welcome_text_elt.text
#
#         assert "Congratulations! You have successfully registered!" == welcome_text
#
#     def test_abs2(self):
#         link = "http://suninjuly.github.io/registration2.html"
#         browser = webdriver.ChromiumEdge()
#         browser.get(link)
#
#         # Ваш код, который заполняет обязательные поля
#         input1 = browser.find_element(by='xpath', value='/html/body/div/form/div[1]/div[1]/input')
#         input1.send_keys("Ivan")
#         input2 = browser.find_element(by='xpath', value='/html/body/div/form/div[1]/div[2]/input')
#         input2.send_keys("Petrov")
#         input3 = browser.find_element(by='xpath', value='/html/body/div/form/div[1]/div[3]/input')
#         input3.send_keys("kirillnnov97@gmail.com")
#         input4 = browser.find_element(by='xpath', value='/html/body/div/form/div[2]/div[1]/input')
#         input4.send_keys("+79991365314")
#         input5 = browser.find_element(by='xpath', value='/html/body/div/form/div[2]/div[2]/input')
#         input5.send_keys("Pochainskaya st.")
#         # Отправляем заполненную форму
#         button = browser.find_element(by='xpath', value='/html/body/div/form/button')
#         button.click()
#
#         # Проверяем, что смогли зарегистрироваться
#         # ждем загрузки страницы
#         time.sleep(1)
#
#         # находим элемент, содержащий текст
#         welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
#         # записываем в переменную welcome_text текст из элемента welcome_text_elt
#         welcome_text = welcome_text_elt.text
#
#         assert "Congratulations! You have successfully registered!" == welcome_text
#
# if __name__ == "__main__":
#     pytest.main()




