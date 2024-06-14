# from selenium import webdriver
# import time
# import math
#
# link = "http://suninjuly.github.io/find_link_text"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     text=str(math.ceil(math.pow(math.pi, math.e) * 10000))
#     print(text)
#     input1 = browser.find_element(by='partial link text', value=text)
#     print(input1)
#     input1.click()
#     input1 = browser.find_element(by='tag name',value='input')
#     print(input1)
#     input1.send_keys("Ivan")
#     input2 = browser.find_element(by='name', value='last_name')
#     print(input2)
#     input2.send_keys("Petrov")
#     input3 = browser.find_element(by='class name', value='city')
#     print(input3)
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element(by='id',value='country')
#     print(input4)
#     input4.send_keys("Russia")
#     button = browser.find_element(by='css selector', value="button.btn")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(40)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
#
# # не забываем оставить пустую строку в конце файла

# ----------------------------------------------------------------------------------------------------------------------
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# link = "http://suninjuly.github.io/find_xpath_form"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     input1 = browser.find_element(by='xpath', value='/html/body/div/form/div[1]/input')
#     input1.send_keys("Ivan")
#     input2 = browser.find_element(by='xpath', value='/html/body/div/form/div[2]/input')
#     input2.send_keys("Petrov")
#     input3 = browser.find_element(by='xpath', value='/html/body/div/form/div[3]/input')
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element(by='xpath', value='/html/body/div/form/div[4]/input')
#     input4.send_keys("Russia")
#     button = browser.find_element(by='xpath', value='/html/body/div/form/div[6]/button[3]')
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
#
# # не забываем оставить пустую строку в конце файла

# ----------------------------------------------------------------------------------------------------------------------

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# try:
#     link = "http://suninjuly.github.io/registration1.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     # Ваш код, который заполняет обязательные поля
#     input1 = browser.find_element(by='xpath', value='/html/body/div/form/div[1]/div[1]/input')
#     input1.send_keys("Ivan")
#     input2 = browser.find_element(by='xpath', value='/html/body/div/form/div[1]/div[2]/input')
#     input2.send_keys("Petrov")
#     input3 = browser.find_element(by='xpath', value='/html/body/div/form/div[1]/div[3]/input')
#     input3.send_keys("kirillnnov97@gmail.com")
#     input4 = browser.find_element(by='xpath', value='/html/body/div/form/div[2]/div[1]/input')
#     input4.send_keys("+79991365314")
#     input5= browser.find_element(by='xpath', value='/html/body/div/form/div[2]/div[2]/input')
#     input5.send_keys("Pochainskaya st.")
#     # Отправляем заполненную форму
#     button = browser.find_element(by='xpath', value='/html/body/div/form/button')
#     button.click()
#
#     # Проверяем, что смогли зарегистрироваться
#     # ждем загрузки страницы
#     time.sleep(1)
#
#     # находим элемент, содержащий текст
#     welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
#     # записываем в переменную welcome_text текст из элемента welcome_text_elt
#     welcome_text = welcome_text_elt.text
#
#     # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
#     assert "Congratulations! You have successfully registered!" == welcome_text
#
# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
#

# -----------------------------------------------------------------------------------------------------------------------

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import math
#
# try:
#     link = "https://suninjuly.github.io/math.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#     number=browser.find_element(by='xpath', value='//*[@id="input_value"]')
#     number= number.text
#     equal= str(math.log(abs(12*math.sin(int(number)))))
#     input2=browser.find_element(by='xpath', value='//*[@id="answer"]')
#     input2.send_keys(equal)
#     input3=browser.find_element(by='xpath', value='//*[@id="robotCheckbox"]')
#     input3.click()
#     input4=browser.find_element(by='xpath', value='//*[@id="robotsRule"]')
#     input4.click()
#     button=browser.find_element(by='xpath', value='/html/body/div/form/button')
#     button.click()
#
#     # input3=browser.find_element(by='xpath', value='//*[@id="robotCheckbox"]')
#     # input1.send_keys("Ivan")
#
# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(5)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
# -----------------------------------------------------------------------------------------------------------------------
# from selenium import webdriver
# import time
# import math
#
#
# link = "https://suninjuly.github.io/get_attribute.html"
#
# try:
#
#     browser = webdriver.ChromiumEdge()
#     browser.get(link)
#     element = browser.find_element(by='xpath', value='//*[@id="treasure"]')
#     number = element.get_attribute('valuex')
#     result = str(math.log(abs(12 * math.sin(int(number)))))
#     input1= browser.find_element(by='xpath', value='//*[@id="answer"]')
#     input1.send_keys(result)
#     input2= browser.find_element(by='xpath', value= '//*[@id="robotCheckbox"]')
#     input2.click()
#     input3= browser.find_element(by='xpath', value= '//*[@id="robotsRule"]')
#     input3.click()
#     button = browser.find_element(by='xpath', value='/html/body/div/form/div/div/button')
#     button.click()
#
#     # input3=browser.find_element(by='xpath', value='//*[@id="robotCheckbox"]')
#     # input1.send_keys("Ivan")
#
# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(2)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
#     #
#     # # не забываем оставить пустую строку в конце файла

#---------------------------------------------------------------------------------------------------

# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.by import By
# import time
#
#
# link= 'https://suninjuly.github.io/selects1.html'
#
# try:
#     browser= webdriver.ChromiumEdge()
#     browser.get(link)
#
#     element = browser.find_element(by='xpath',value='//*[@id="num1"]')
#     term1=element.text
#     element = browser.find_element(by='xpath', value='//*[@id="num2"]')
#     term2=element.text
#
#     summary = int(term1)+int(term2)
#
#     print(summary)
#
#     select = Select(browser.find_element(by='id', value="dropdown"))
#     select.select_by_value(str(summary))
#
#     button = browser.find_element(by='xpath', value='/html/body/div/form/button')
#     button.click()
#
# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(5)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
#
#     # # не забываем оставить пустую строку в конце файла

#---------------------------------------------------------------------------------------------------

# from selenium import webdriver
# import math
# import time
#
# link= 'https://suninjuly.github.io/execute_script.html'
# try:
#      browser = webdriver.ChromiumEdge()                                         #Переходим по ссылке
#      browser.get(link)
#
#      element= browser.find_element(by='xpath', value='//*[@id="input_value"]')  #Читаем значение X из выражения
#      number= element.text
#
#      result= str(math.log(abs(12 * math.sin(int(number)))))                     #Счиатем значение выражения
#
#      input1= browser.find_element(by='xpath', value='//*[@id="answer"]')        #Отправляем значение в строку ввода
#      input1.send_keys(result)
#
#      input2= browser.find_element(by='xpath', value='//*[@id="robotCheckbox"]') #Кликаем на чекбокс I'm the robot
#      input2.click()
#
#      input3 = browser.find_element(by= 'xpath', value='//*[@id="robotsRule"]')
#      browser.execute_script("return arguments[0].scrollIntoView(true);", input3)
#      input3.click()
#
#
#      button= browser.find_element(by='xpath', value='/html/body/div/form/button')        #
#      button.click()
#
# finally:
#      time.sleep(10)
#      browser.quit()
#
# ###
#
# ###

#---------------------------------------------------------------------------------------------------

# from selenium import webdriver
# import time
#
# link = 'https://suninjuly.github.io/file_input.html'
#
# try:
#     browser = webdriver.ChromiumEdge()
#     browser.get(link)
#
#     input1= browser.find_element(by='xpath', value='/html/body/div/form/div/input[1]')        #Отправляем значение в строку ввода
#     input1.send_keys('Kirill')
#
#     input2 = browser.find_element(by='xpath',value='/html/body/div/form/div/input[2]')  # Отправляем значение в строку ввода
#     input2.send_keys('Zhukov')
#
#     input3 = browser.find_element(by='xpath',value='/html/body/div/form/div/input[3]')  # Отправляем значение в строку ввода
#     input3.send_keys('kirillnnov97@yandex.ru')
#
#     send_button = browser.find_element(by='xpath', value='//*[@id="file"]')
#     send_button.send_keys(r'C:\Users\kiril\OneDrive\Desktop\Текстовый документ.txt')
#
#     button = browser.find_element(by='xpath', value='/html/body/div/form/button')
#     button.click()
#
# finally:
#      time.sleep(10)
#      browser.quit()

###

###
#---------------------------------------------------------------------------------------------------
# from selenium import webdriver
# import math
# import time
#
# link = 'https://suninjuly.github.io/alert_accept.html'
#
# try:
#     browser = webdriver.ChromiumEdge()
#     browser.get(link)
#
#     blueButton= browser.find_element(by= 'xpath', value='/html/body/form/div/div/button')
#     blueButton.click()
#
#     confirm = browser.switch_to.alert
#     confirm.accept()
#
#     x_element= browser.find_element(by='xpath', value='//*[@id="input_value"]').text
#     result=math.log(abs(12*math.sin(int(x_element))))
#
#     input1= browser.find_element(by='xpath', value='//*[@id="answer"]')
#     input1.send_keys(result)
#
#     submit_button= browser.find_element(by='xpath', value='/html/body/form/div/div/button')
#     submit_button.click()
#
# finally:
#      time.sleep(5)
#      browser.quit()
#
# ##
#
# ##
#---------------------------------------------------------------------------------------------------

# from selenium import webdriver
# import math
# import time
#
# link = 'http://suninjuly.github.io/redirect_accept.html'
# try:
#     browser = webdriver.ChromiumEdge()
#     browser.get(link)
#
#     troll_button= browser.find_element(by='xpath', value='/html/body/form/div/div/button')
#     troll_button.click()
#
#     new_window = browser.window_handles[1]
#     browser.switch_to.window(new_window)
#
#     x_element= browser.find_element(by='xpath', value='//*[@id="input_value"]').text
#     result=math.log(abs(12*math.sin(int(x_element))))
#
#     input1= browser.find_element(by='xpath', value='//*[@id="answer"]')
#     input1.send_keys(result)
#
#     submit_button= browser.find_element(by='xpath', value='/html/body/form/div/div/button')
#     submit_button.click()
#
# finally:
#      time.sleep(5)
#      browser.quit()
#
# ##
#
# ##

#---------------------------------------------------------------------------------------------------
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# browser = webdriver.ChromiumEdge()
# browser.get("http://suninjuly.github.io/wait1.html")
#
# time.sleep(2)
# button = browser.find_element(By.ID, "verify")
# button.click()
# message = browser.find_element(By.ID, "verify_message")
#
# assert "successful" in message.text
#---------------------------------------------------------------------------------------------------
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# browser = webdriver.ChromiumEdge()
# # говорим WebDriver искать каждый элемент в течение 5 секунд
# browser.implicitly_wait(5)
#
# browser.get("http://suninjuly.github.io/cats.html")
#
# button = browser.find_element(By.ID, "button")
# button.click()
# message = browser.find_element(By.ID, "verify_message")
#
# assert "successful" in message.text
#---------------------------------------------------------------------------------------------------
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# import time
# import math
#
# link= 'https://suninjuly.github.io/explicit_wait2.html'
#
# try:
#     browser = webdriver.ChromiumEdge()
#     browser.get(link)
#     browser.implicitly_wait(5)
#
#
#
#     price_value = WebDriverWait(browser, 12).until(
#         EC.text_to_be_present_in_element((By.ID, "price"),"100")
#     )
#     button=browser.find_element(by='xpath', value='//*[@id="book"]')
#     button.click()
#
#     x_element= browser.find_element(by='xpath', value='//*[@id="input_value"]').text
#     result=math.log(abs(12*math.sin(int(x_element))))
#
#     input_result= browser.find_element(by='xpath',value='//*[@id="answer"]')
#     input_result.send_keys(result)
#
#     button2= browser.find_element(by='xpath', value='//*[@id="solve"]')
#     button2.click()
#
# finally:
#     time.sleep(15)
#
#     browser.quit()
#
#     #


# print("Let's count together: {}, then goes {}, and then {}".format("one", "two", "three"))

# ---------------------------------------------------------------------------------------------------
import pytest
from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.by import By
class TestAbs(unittest.TestCase):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.ChromiumEdge()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(by='xpath', value='/html/body/div/form/div[1]/div[1]/input')
        input1.send_keys("Ivan")
        input2 = browser.find_element(by='xpath', value='/html/body/div/form/div[1]/div[2]/input')
        input2.send_keys("Petrov")
        input3 = browser.find_element(by='xpath', value='/html/body/div/form/div[1]/div[3]/input')
        input3.send_keys("kirillnnov97@gmail.com")
        input4 = browser.find_element(by='xpath', value='/html/body/div/form/div[2]/div[1]/input')
        input4.send_keys("+79991365314")
        input5= browser.find_element(by='xpath', value='/html/body/div/form/div[2]/div[2]/input')
        input5.send_keys("Pochainskaya st.")
        # Отправляем заполненную форму
        button = browser.find_element(by='xpath', value='/html/body/div/form/button')
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        assert "Congratulations! You have successfully registered!" == welcome_text
        assert "Congratulations! You have successfully registered!" != 1

    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.ChromiumEdge()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(by='xpath', value='/html/body/div/form/div[1]/div[1]/input')
        input1.send_keys("Ivan")
        input2 = browser.find_element(by='xpath', value='/html/body/div/form/div[1]/div[2]/input')
        input2.send_keys("Petrov")
        input3 = browser.find_element(by='xpath', value='/html/body/div/form/div[1]/div[3]/input')
        input3.send_keys("kirillnnov97@gmail.com")
        input4 = browser.find_element(by='xpath', value='/html/body/div/form/div[2]/div[1]/input')
        input4.send_keys("+79991365314")
        input5 = browser.find_element(by='xpath', value='/html/body/div/form/div[2]/div[2]/input')
        input5.send_keys("Pochainskaya st.")
        # Отправляем заполненную форму
        button = browser.find_element(by='xpath', value='/html/body/div/form/button')
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        assert "Congratulations! You have successfully registered!" == welcome_text

if __name__ == "__main__":
    pytest.main()












