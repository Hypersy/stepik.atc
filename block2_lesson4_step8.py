from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


def calc(value):
    return str(math.log(abs(12 * math.sin(int(value)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")
# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100"))
browser.find_element(By.CSS_SELECTOR, 'button[id="book"]').click()                                      

x_element = browser.find_element_by_id('input_value').text
y = calc(x_element)

#driver.execute_script("window.scrollBy(0, 100);")
inter = browser.find_element_by_id("answer")
inter.send_keys(y)
    
button = browser.find_element_by_id("solve") .click()

#x = int(browser.find_element_by_id('input_value').text)
#answer_input = browser.find_element_by_id('answer').send_keys(calc(x))
#browser.find_element_by_css_selector('button[type="submit"]').click()


time.sleep(9)
browser.quit()