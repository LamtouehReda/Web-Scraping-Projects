from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import pandas as pd

csv_file=open('top250MoviesIMDB.csv','w',encoding='utf8')
columns=['Name','Release','Director','Stars']
writer=csv.DictWriter(csv_file,fieldnames=columns)
writer.writeheader()

url = 'https://www.imdb.com/chart/top/'
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)


for i in range(5): #put 250 instead of 5
	movies=driver.find_elements_by_class_name('posterColumn')
	link=movies[i].find_element_by_tag_name('a')
	link.click()
	movie_name=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.TAG_NAME,'h1'))).text
	movie_release=driver.find_element_by_css_selector('a.ipc-link.ipc-link--baseAlt.ipc-link--inherit-color.sc-52284603-1.ifnKcw').text
	movie_director=driver.find_element_by_css_selector('a.ipc-metadata-list-item__list-content-item.ipc-metadata-list-item__list-content-item--link').text
	stars=driver.find_elements_by_css_selector('ul.ipc-inline-list.ipc-inline-list--show-dividers.ipc-inline-list--inline.ipc-metadata-list-item__list-content.baseAlt')[2]
	stars=stars.find_elements_by_tag_name('a')
	stars_names=[]
	for star in stars:
		stars_names.append(star.text)
	writer.writerow({'Name':movie_name,'Release':movie_release,
							'Director':movie_director,'Stars':','.join(stars_names)})
	driver.back()
	driver.implicitly_wait(3)



csv_file.close()

csv_data=pd.read_csv('top250MoviesIMDB.csv',encoding='utf8')
xl_file=pd.ExcelWriter('top250MoviesIMDB.xlsx')
csv_data.to_excel(xl_file,index=False)
xl_file.save()

driver.quit()