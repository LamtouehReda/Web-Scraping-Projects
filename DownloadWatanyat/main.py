from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions() 

download_dir = r"C:\Users\Lenovo\OneDrive\Bureau\exams\svt"

options.add_experimental_option('prefs',{"download.default_directory": download_dir,
	"download.prompt_for_download": False,"plugins.always_open_pdf_externally": True})

driver=webdriver.Chrome(ChromeDriverManager().install(),options=options)
driver.get('https://moutamadris.ma/%d8%a7%d9%85%d8%aa%d8%ad%d8%a7%d9%86%d8%a7%d8%aa-%d9%88%d8%b7%d9%86%d9%8a%d8%a9-%d8%b9%d9%84%d9%88%d9%85-%d8%a7%d9%84%d8%ad%d9%8a%d8%a7%d8%a9-%d9%88%d8%a7%d9%84%d8%a7%d8%b1%d8%b6-%d8%a7%d9%84%d8%ab/')

exams1=driver.find_elements_by_link_text('تحميل')
for i in range(len(exams1)):
	exams=driver.find_elements_by_link_text('تحميل')
	pdf_url=exams[i].get_attribute('href')
	driver.get(pdf_url)
	time.sleep(3)

