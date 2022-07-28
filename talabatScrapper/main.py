import csv
import pandas as pd
import locale
import mysql.connector
import re
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database='talabat3'
)
mycursor = mydb.cursor()

def prepareQuery(name):
	name=name.replace(' ','_')
	s=f"CREATE TABLE {name} ( categorie VARCHAR(10000), meals TEXT )"
	
	return s



base_url='https://www.talabat.com/ar/ksa/restaurants/169/al-aqiq'
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get(base_url)

restaurents=WebDriverWait(driver,20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'div.list-itemstyles__VendorListItemContainer-sc-ia2hbn-0.gINWsk')))
for i in range(len(restaurents)):
	restaurents=WebDriverWait(driver,20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'div.list-itemstyles__VendorListItemContainer-sc-ia2hbn-0.gINWsk')))
	name=restaurents[i].find_element_by_tag_name('h2').text
	link=restaurents[i].find_element_by_tag_name('a').get_attribute('href')
	restaurents[i].click()
	menu=WebDriverWait(driver,20).until(EC.presence_of_element_located((By.CSS_SELECTOR,'div.menu-categoriesstyles__MenuCategoriesContainer-sc-1enqip-0.ikzMlv')))
	categories=menu.find_elements_by_css_selector('div.clickable.mb-2.muted.category-nav.d-inline-block.pr-1.truncate.w-100 ')
	categories_names=[cat.text for cat in categories]

	mycursor.execute(prepareQuery(name))

	csv_file=open(f'{name}.csv','w',encoding='utf-8-sig')
	locale.setlocale(locale.LC_ALL, '')
	DELIMITER=';' if locale.localeconv()['decimal_point'] == ',' else ','
	writer=csv.writer(csv_file,dialect='excel', delimiter=DELIMITER)
	# try:
	categories=WebDriverWait(driver,40).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'div.accordionstyle__AccordionContainer-sc-h3jkuk-0.cXuoK')))
	for i in range(len(categories)):
		meals=categories[i].find_elements_by_css_selector('div.f-15')
		meals=[meal.text for meal in meals]
		row=[categories_names[i]]+meals
		name=name.replace(' ','_')
		sql=f"INSERT INTO {name} (categorie,meals) VALUES (%s,%s)"
		meals=[meal.replace(' ','_') for meal in meals]
		meals=','.join(meals)
		categorie=categories_names[i].replace(' ','_')
		val=(categorie,meals)
		mycursor.execute(sql,val)
		mydb.commit()
		writer.writerow(row)
	csv_file.close()

	# except:
	# 	pass
	driver.back()
driver.close()


