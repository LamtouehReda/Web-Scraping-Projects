import requests
from bs4 import BeautifulSoup
import csv
import json

url='https://zobraa.000webhostapp.com/category.php?cat=programming'
soup=BeautifulSoup(requests.get(url).content,'lxml')

posts_titles=[post.find('h4').text for post in soup.find_all('div',{'class':'blog-meta big-meta col-md-8'})]
url_base='https://zobraa.000webhostapp.com/'
posts_images=[post.find('img').attrs['src'] for post in soup.find_all('div',{'class':'post-media'})]
posts_images=[url_base+src for src in posts_images]

csv_file=open('programmingArticles.csv','w')
json_file=open('programmingArticles.json','w')

columns=['Title','Image']
data={}

writer=csv.DictWriter(csv_file,fieldnames=columns)
writer.writeheader()
for i in range(len(posts_titles)):
	writer.writerow({'Title':posts_titles[i],'Image':posts_images[i]})
	data['Title']=posts_titles[i]
	data['Image']=posts_images[i]
	json_data=json.dumps(data)
	json_file.write(json_data+'\n')

csv_file.close()
json_file.close()
