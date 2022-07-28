import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

os.chdir(r"C:\Users\Lenovo\OneDrive\Bureau\Web Scrapping\Downloads")

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://www.instgram.com")

#delay the action for 10 seconds until loading the HTML and CSS code
username=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name='username']")))
password=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name='password']")))

username.clear()
username.send_keys("32983298")
password.clear()
password.send_keys('Reda Test')

button=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[type='submit']"))).click()
