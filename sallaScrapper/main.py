from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json

json_file=open('salla.json','w')


options = webdriver.ChromeOptions()
# options.add_argument('headless')

base_url='https://ofour.com/en-ae/category/sneakers/jordans/air-jordans/'
driver=webdriver.Chrome(ChromeDriverManager().install(),options=options)
driver.get(base_url)

products_finale=[]

products=WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'div.archive_product_each.dib')))
prices=WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.TAG_NAME,'bdi')))
prices=[price.text[4:] for price in prices]

for i in range(len(products)):
	pro_dict=dict()
	brand=products[i].find_element_by_css_selector('a.product_brand')
	pro_dict['brand']=brand.find_element_by_tag_name('h4').text
	product_title=products[i].find_element_by_css_selector('a.product_title')
	pro_dict['title']=product_title.find_element_by_tag_name('h4').text
	pro_dict['price']=prices[i]
	products_finale.append(pro_dict)


links=WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'a.archive_product_image')))


for i in range(len(links)):
	time.sleep(2)
	links=WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'a.archive_product_image')))
	links[i].click()
	product_images=[]
	images=WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'div.slick-slide')))
	images=[div.find_element_by_tag_name('img') for div in images]
	images1=[img.get_attribute('src') for img in images]
	images2=[img.get_attribute('data-zoom-image') for img in images]
	products_finale[i]['images']=images2
	driver.back()

print(products_finale)
for p in products_finale:
	json_file.write(json.dumps(p)+'\n')
json_file.close()
driver.close()
