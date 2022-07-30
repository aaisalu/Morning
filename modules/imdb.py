from bs4 import BeautifulSoup
import requests,csv

url=input("Please feed the imdb website: ")
def imdb_v1(url):		
	pop=requests.get(url).text
	Soup=BeautifulSoup(pop,'lxml')
	ids=Soup.find_all('div',class_="lister-item mode-advanced")
	for box in ids:
		Title=box.h3.a.text
		Year=(box.find('span',class_="lister-item-year text-muted unbold")).text
		rating=(box.find('div',class_='inline-block ratings-imdb-rating')).strong.text
		votes=(box.find('p',class_='sort-num_votes-visible')).find_all('span')[1].text
		# NOTE:
		# YOU CA find the find_all by adding {} like a dictionary and get the data
		# if there is dulicate vakues like {'name':'nv'} then you can use {} dictionary method
		# to slice the data .SLice the data accoring to it.

		# Remember find_ALL is depreciated in bs4 instead use find_all

		# like in Money code there is no Gross in first index but there is in second index.
		# so overcome error we convert into len()>1 if found gives tthe bank[1]

		bank=box.find_all('span',{'name':'nv'})
		Money=bank[1].text if len(bank)>1 else 'No any, Data Found'
		
		summary=(box.find_all('p',class_='text-muted')[-1]).text.strip()

		# Time=(box.find('p').text).replace('|',' ').replace(' ','').strip()
		
		Time=(box.find('p',class_='text-muted')).find('span',class_='runtime').text
		types=(((box.find('p',class_='text-muted').find('span',class_='genre'))).text).strip()
		with open('Imdb_v1.csv',newline='',mode='a+') as fire:
			spam=csv.writer(fire,delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
			spam.writerow([Title,summary,types,Time,Money,Year,rating,votes])

imdb_v1()