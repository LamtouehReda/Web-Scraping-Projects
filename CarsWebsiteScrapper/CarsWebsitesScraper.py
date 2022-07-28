import requests 
import csv
from bs4 import BeautifulSoup
import json
import pandas as pd

csv_file=open('CarsWebsiteScrapper.csv','w')
json_file=open('CarsWebsiteScrapper.json','w')
columns=['name','miles','price','dealer','rating','reviews','image']
writer=csv.DictWriter(csv_file,fieldnames=columns)
writer.writeheader()

for j in range(1,5):
	data={}
	url=f'https://www.cars.com/shopping/results/?page={j}&page_size=20&list_price_max=&makes[]=mercedes_benz&maximum_distance=20&models[]=&stock_type=all&zip='
	soup=BeautifulSoup(requests.get(url).content,'lxml')
	names=[x.text for x in soup.find_all('h2',{'class':'title'})]
	miles=[x.text for x in soup.find_all('div',{'class':'mileage'})[1:]]
	prices=[x.text for x in soup.find_all('span',{'class':'primary-price'})]
	dealers=[x.find('strong').text for x in soup.find_all('div',{'class':'dealer-name'})]
	ratings=[x.text for x in soup.find_all('span',{'class':'sds-rating__count'})]
	reviews=[x.text[1:-1] for x in soup.find_all('span',{'class':'sds-rating__link sds-button-link'})]
	images=[x.find('img') for x in soup.find_all('div',{'class':'image-wrap','data-index':'0'})]
	for i in range(len(images)):
		try:
			images[i]=images[i]['data-src']
		except:
			images[i]=images[i]['src']

	for k in range(len(names)):
		writer.writerow({'name':names[k],'miles':miles[k],
			             'price':prices[k],'dealer':dealers[k],
			             'rating':ratings[k],'reviews':reviews[k],
			             'image':images[k]})

		data['name']=names[k]
		data['miles']=miles[k]
		data['price']=prices[k]
		data['dealer']=dealers[k]
		data['rating']=ratings[k]
		data['reviews']=reviews[k]
		data['image']=images[k]
		json_data=json.dumps(data)

		json_file.write(json_data+'\n')

csv_file.close()
json_file.close()

csv_data=pd.read_csv('CarsWebsiteScrapper.csv')
xl_file=pd.ExcelWriter('CarsWebsiteScrapper.xlsx')
csv_data.to_excel(xl_file,index=False)
xl_file.save()
