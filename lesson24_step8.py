from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
	browser = webdriver.Chrome()
	browser.get("http://suninjuly.github.io/explicit_wait2.html")

	# говорим Selenium проверять в течение 15 секунд, пока цена не снизится до $100
	price = WebDriverWait(browser, 15).until(
			EC.text_to_be_present_in_element((By.ID, 'price'), '100')
		)
	button = browser.find_element(By.ID, 'book')
	button.click()
	
	x_element = browser.find_element(By.ID, 'input_value')
	x = x_element.text
	y = calc(x)
	
	input_answer = browser.find_element(By.ID, 'answer')
	input_answer.send_keys(y)
	
	button = browser.find_element(By.ID, 'solve')
	button.click()	

finally:
    print(browser.switch_to.alert.text)
    browser.quit()

