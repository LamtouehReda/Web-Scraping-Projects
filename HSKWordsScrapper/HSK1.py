import requests 
from bs4 import BeautifulSoup

url='https://www.digmandarin.com/hsk-1-vocabulary-list.html'

for i in range(1,7):
	url=f'https://www.digmandarin.com/hsk-{i}-vocabulary-list.html'
	soup=BeautifulSoup(requests.get(url).content,'lxml')
	words=soup.find_all('td',{'class':'tg-yw4l'})
	words=[word.text for word in words]
	words=[word for word in words if (word > u'\u4e00' and word < u'\u9fff')]
	print('\n'.join(words))
	print(len(words))
	print('---------------------------------------------')
	# for word in words:
	# 	if word > u'\u4e00' and word < u'\u9fff':
	# 		print(word)
