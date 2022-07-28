import os
import shutil
import time
import random
import string
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions() 

download_dir = r'C:\Users\Lenovo\OneDrive\Bureau\Web Scrapping\kotobiScrapper'


options.add_experimental_option('prefs',{"download.default_directory": download_dir})
options.add_argument("start-maximized")
options.add_extension(r'C:\Users\Lenovo\OneDrive\Bureau\Web Scrapping\extension_4_44_0_0.crx')
# options.add_argument("--auto-open-devtools-for-tabs")
# options.add_argument('headless')

base_url='https://ktby.net/'
driver=webdriver.Chrome(ChromeDriverManager().install(),options=options)
driver.get(base_url)

time.sleep(5)

def join_courses(coursesUls):
	courses=[]
	for coursesUl in coursesUls:
		courses+=coursesUl.find_elements_by_css_selector('a.pointer')
	return courses

def get_page_courses(driver):
	coursesUl=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.list-cards')))
	# courses=join_courses(coursesUls)
	courses=coursesUl.find_elements_by_css_selector('a.pointer')
	return courses

def download_pdfs(driver):
	pdfs=driver.find_elements_by_link_text('التحميل')
	pdfs_no_downloadable=driver.find_elements_by_link_text('فهرس الدروس')
	videos=driver.find_elements_by_id('video-player')
	print(len(videos))
	course=driver.find_elements_by_css_selector('.list-cards')
	if len(pdfs)>=1 or len(pdfs_no_downloadable)>=1 or len(videos)>=1 or len(course)==0:
		return True
	return False

def get_file_url(driver):
	pdfs=driver.find_elements_by_link_text('التحميل')
	pdfs_no_downloadable=driver.find_elements_by_link_text('فهرس الدروس')
	videos=driver.find_elements_by_id('video-player')
	if len(pdfs)>=1:
		return pdfs[0].get_attribute('href')
	elif len(pdfs_no_downloadable)>=1:
		return 'No Downloadable'
	elif len(videos)>=1:
		href=driver.find_element_by_tag_name('iframe').get_attribute('src')
		return href
	else:
		return 'No File'

def write_text_file(dir,url):
	file=open(f'{dir}\\Info.txt','w')
	file.write(url)
	file.close()

titles=[]
def loop_through_page_courses(driver,parent_dir,titles):

	courses=get_page_courses(driver)

	for i in range(len(courses)):

		courses=get_page_courses(driver)
		grandparent = courses[i].find_element_by_xpath('../../..')
		display=grandparent.value_of_css_property('display')
		# driver.execute_script("arguments[0].style.display = 'block';", grandparent)
		title=courses[i].find_element_by_css_selector('div.ctitle')
		title=title.find_element_by_tag_name('span').text
		
		if display!='none':

			sub_dir=f'{parent_dir}\\{title}'
			print(sub_dir)
			try:
				os.mkdir(sub_dir)
			except:
				random_string=''.join(random.choices(string.ascii_uppercase + string.digits, k=20))
				sub_dir=f'{parent_dir}\\{random_string}'
				os.mkdir(sub_dir)


			courses[i].click()

			if download_pdfs(driver)==True:
				url=get_file_url(driver)
				write_text_file(sub_dir,url)
				driver.back()
				time.sleep(3)
				continue
			else:	
				loop_through_page_courses(driver,sub_dir,titles)
			driver.back()
			time.sleep(3)


try:
	parent_dir=r'C:\Users\Lenovo\OneDrive\Bureau\Web Scrapping\kotobiScrapper'
	loop_through_page_courses(driver,parent_dir,[])
finally:
	driver.quit()

