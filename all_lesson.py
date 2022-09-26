from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select
import os

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# link = "http://suninjuly.github.io/find_xpath_form"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     input1 = browser.find_element_by_tag_name("input")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element_by_name("last_name")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element_by_class_name("form-control.city")
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element_by_id("country")
#     input4.send_keys("Russia")
#     button = browser.find_element_by_xpath("//button[@type='submit']")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()



# link = "https://suninjuly.github.io/math.html"
#
# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     x_element = browser.find_element_by_id("input_value")
#     x = x_element.text
#     y = calc(x)
#
#     input1 = browser.find_element_by_id("answer")
#     input1.send_keys(y)
#
#     option1 = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
#     option1.click()
#
#     option2 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
#     option2.click()
#
#     button = browser.find_element_by_xpath("//button[@type='submit']")
#     button.click()
#
#
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()


# link = "http://suninjuly.github.io/get_attribute.html"
#
# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     x_element = browser.find_element_by_id("treasure")
#     treasure_checked = x_element.get_attribute("valuex")
#
#     y = calc(treasure_checked)
#
#     input1 = browser.find_element_by_id("answer")
#     input1.send_keys(y)
#
#     option1 = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
#     option1.click()
#
#     option2 = browser.find_element(By.CSS_SELECTOR, "[value='robots']")
#     option2.click()
#
#     button = browser.find_element_by_xpath("//button[@type='submit']")
#     button.click()
#
#
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()


link = "http://suninjuly.github.io/selects1.html"


#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     num1 = browser.find_element_by_id("num1").text
#     num2 = browser.find_element_by_id("num2").text
#
#     sum = int(num1) + int(num2)
#
#     select = Select(browser.find_element_by_id("dropdown"))
#     select.select_by_value(str(sum))
#     time.sleep(2)
#
#     browser.find_element_by_xpath("//button[@type='submit']").click()
#
#
#
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(5)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

#2-2

#
# link = "https://suninjuly.github.io/execute_script.html"
#
# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     x_element = browser.find_element_by_id("input_value")
#     x = x_element.text
#     y = calc(x)
#     browser.execute_script("window.scrollBy(0, 100);")
#     input1 = browser.find_element_by_id("answer")
#     input1.send_keys(y)
#
#     option1 = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
#     option1.click()
#
#     option2 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
#     option2.click()
#
#     button = browser.find_element_by_xpath("//button[@type='submit']")
#     button.click()
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
#

#2-2-3

#
# link = "http://suninjuly.github.io/file_input.html"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     input1 = browser.find_element_by_tag_name("input")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element_by_name("lastname")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element_by_name("email")
#     input3.send_keys("der@de.com")
#
#     element = browser.find_element_by_name("file")
#
#     current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
#     file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
#     element.send_keys(file_path)
#
#     button = browser.find_element_by_xpath("//button[@type='submit']")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()


#2-3-1


# link = "http://suninjuly.github.io/alert_accept.html"
#
# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     browser.find_element_by_xpath("//button[@type='submit']").click()
#
#     confirm = browser.switch_to.alert
#     confirm.accept()
#     time.sleep(2)
#     x_element = browser.find_element_by_id("input_value")
#     x = x_element.text
#     y = calc(x)
#
#     input1 = browser.find_element_by_id("answer")
#     input1.send_keys(y)
#
#     button = browser.find_element_by_xpath("//button[@type='submit']")
#     button.click()
#
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(20)
#     # закрываем браузер после всех манипуляций
#     browser.quit()


#2-3-2

# link = "http://suninjuly.github.io/redirect_accept.html"
#
#
# def calc(x):
#     return str(math.log(abs(12 * math.sin(int(x)))))
#
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     browser.find_element_by_xpath("//button[@type='submit']").click()
#
#     new_window = browser.window_handles[1]
#     browser.switch_to.window(new_window)
#
#     x_element = browser.find_element_by_id("input_value")
#     x = x_element.text
#     y = calc(x)
#
#     input1 = browser.find_element_by_id("answer")
#     input1.send_keys(y)
#
#     time.sleep(1)
#     button = browser.find_element_by_xpath("//button[@type='submit']")
#     button.click()
#
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(20)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

#41-1

# link = "http://suninjuly.github.io/cats.html"
#
#
# def calc(x):
#     return str(math.log(abs(12 * math.sin(int(x)))))
#
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     browser.find_element(By.ID, "button")
#
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(20)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

#41-1


link = "http://suninjuly.github.io/explicit_wait2.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element_by_id("book")
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    button1.click()

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    time.sleep(1)
    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()