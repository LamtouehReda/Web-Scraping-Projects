from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://orteil.dashnet.org/cookieclicker/')

driver.implicitly_wait(5)

cookie=driver.find_element_by_id('bigCookie')
cookiesNumber=driver.find_element_by_id('cookies')

items=[driver.find_element_by_id(f'productPrice{i}') for i in range(1,-1,-1)]

actions=ActionChains(driver)
actions.click(cookie)

for i in range(5000):
	actions.perform()
	count=int(cookiesNumber.text.split(' ')[0])
	for item in items:
		value=int(item.text)
		if value<=count:
			upgrad_actions=ActionChains(driver)
			upgrad_actions.move_to_element(item)
			upgrad_actions.click()
			upgrad_actions.perform()

 