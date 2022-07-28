import os
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from interface import *

def addSS(url):
		newurl=[]
		for i in range(len(url)):
			if i==12:
				newurl.append('ss')
			newurl.append(url[i])
		return ''.join(newurl)

def download(url):
	options = webdriver.ChromeOptions() 

	download_dir = r"C:\Users\Lenovo\OneDrive\Bureau\Python\Web Scrapping\YoutubePlaylistDownloader"

	options.add_experimental_option('prefs',{"download.default_directory": download_dir})
	# options.add_argument('headless')
	options.add_extension(r'C:\Users\Lenovo\OneDrive\Bureau\Python\Web Scrapping\extension_4_44_0_0.crx')


	# url='https://www.youtube.com/playlist?list=PLzMcBGfZo4-kCLWnGmK0jUBmGLaJxvi4j'
	driver=webdriver.Chrome(ChromeDriverManager().install(),options=options)
	driver.get(url)

	driver.implicitly_wait(5)

	videos_names=driver.find_elements_by_id('video-title')

	playlist=driver.find_elements_by_tag_name('ytd-playlist-video-renderer')
	
	for i in range(len(playlist)):
		try:
			playlist=driver.find_elements_by_tag_name('ytd-playlist-video-renderer')
			link=playlist[i].find_element_by_tag_name('ytd-thumbnail')
			href=link.find_element_by_css_selector('.yt-simple-endpoint.inline-block.style-scope.ytd-thumbnail').get_attribute('href')
			driver.get(addSS(href))
			downloadBtn=WebDriverWait(driver,30).until(EC.presence_of_element_located((By.CSS_SELECTOR,'a.link.link-download.subname.ga_track_events.download-icon')))
			driver.get(downloadBtn.get_attribute('href'))
			driver.back()
			driver.implicitly_wait(3)
		except:
			pass

	for name in videos_names:
		print(name.text)
		while not os.path.exists(f'{download_dir}\\{name.text}.mp4'):
			time.sleep(1)
	driver.quit()


root=tk.Tk()
Window(root,'YPD','200x50',download)


