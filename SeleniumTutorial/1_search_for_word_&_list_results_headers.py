from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# url='https://www.techwithtim.net/'
url='https://zobraa.000webhostapp.com/'
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)

search=driver.find_element_by_class_name('form-group')
search=search.find_element_by_name('search')
search.clear()
search.send_keys('linux')
search.send_keys(Keys.RETURN)

try:
	container=WebDriverWait(driver,30).until(EC.presence_of_element_located((By.CLASS_NAME,'page-wrapper')))
	articles=container.find_elements_by_tag_name('h4')
	for article in articles:
		title=article.find_element_by_tag_name('a')
		print(title.text)
finally:
	driver.quit()
