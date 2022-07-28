from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://twitter.com/i/flow/login')

def multiCssSelector(tag,cssSelector):
	return tag+'.'+cssSelector.replace(' ','.')

UsernameInptCssSelector='input.r-30o5oe.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-t60dpp.r-1dz5y72.r-fdjqy7.r-13qz1uu'
NxtBtnCssSelector='div.css-18t94o4.css-1dbjc4n.r-sdzlij.r-1phboty.r-rs99b7.r-ywje51.r-usiww2.r-2yi16.r-1qi8awa.r-1ny4l3l.r-ymttw5.r-o7ynqc.r-6416eg.r-lrvibr.r-13qz1uu'
PassInptCssSelector='input.r-30o5oe.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-t60dpp.r-1dz5y72.r-fdjqy7.r-13qz1uu'
submitBtnCssSelector='div.css-18t94o4.css-1dbjc4n.r-sdzlij.r-1phboty.r-rs99b7.r-ywje51.r-usiww2.r-peo1c.r-1ps3wis.r-1ny4l3l.r-1guathk.r-o7ynqc.r-6416eg.r-lrvibr.r-13qz1uu'
searchCssSelector=multiCssSelector('input','r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-xyw6el r-13rk5gd r-1dz5y72 r-fdjqy7 r-13qz1uu')
followBtnCssSelector=multiCssSelector('div','css-18t94o4 css-1dbjc4n r-42olwf r-sdzlij r-1phboty r-rs99b7 r-15ysp7h r-4wgw6l r-1ny4l3l r-ymttw5 r-o7ynqc r-6416eg r-lrvibr')

username=WebDriverWait(driver,20).until(EC.presence_of_element_located((By.CSS_SELECTOR,UsernameInptCssSelector)))
username.clear()
username.send_keys('SrakataDev')
time.sleep(5)

nextBtn=WebDriverWait(driver,20).until(EC.presence_of_element_located((By.CSS_SELECTOR,NxtBtnCssSelector)))
nextBtn.click()
time.sleep(5)

password=WebDriverWait(driver,20).until(EC.presence_of_element_located((By.CSS_SELECTOR,PassInptCssSelector)))
password.send_keys('Reda1949')
time.sleep(5)

login=WebDriverWait(driver,20).until(EC.presence_of_element_located((By.CSS_SELECTOR,submitBtnCssSelector)))
login.click()
time.sleep(5)

searchInpt=WebDriverWait(driver,20).until(EC.presence_of_element_located((By.CSS_SELECTOR,searchCssSelector)))
searchInpt.clear()
searchInpt.send_keys('NASA')
searchInpt.send_keys(Keys.RETURN)
time.sleep(5)

try:
	account=WebDriverWait(driver,20).until(EC.presence_of_element_located((By.CSS_SELECTOR,followBtnCssSelector)))
	account.click()
except:
	print('account doesnt exist')
finally:
	driver.quit()