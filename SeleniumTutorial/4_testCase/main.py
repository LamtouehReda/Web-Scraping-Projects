import unittest
from selenium import webdriver
import page 
from webdriver_manager.chrome import ChromeDriverManager

class PythonOrgSearch(unittest.TestCase):

	def setUp(self):
		self.driver=webdriver.Chrome(ChromeDriverManager().install())
		self.driver.get('http://www.python.org')


	def test_search_python(self):
		mainPage=page.MainPage(self.driver)
		assert mainPage.is_title_matches()
		mainPage.search_text_element='pycon'
		search_result_page=page.SearchResultPage(self.driver)
		assert search_result_page.is_results_found()

	def tearDown(self):
		self.driver.close()


if __name__=='__main__':
	unittest.main()