from bs4 import BeautifulSoup
import requests,csv

url=input("Please feed the imdb website: ")


def imdb_v5(url):
	# url='https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc&count=100&start=%27+str(hi)+%27&ref_=adv_nxt'
	incoming=requests.get(url).text
	soup=BeautifulSoup(incoming,'lxml')
	data=soup.find_all('div',{"class":'lister-item mode-advanced'})
	for index,box in enumerate(data):

		title=box.h3.a.text
		year=box.find('span',class_='lister-item-year text-muted unbold').text.replace('(','').replace(')','')
		rating=box.find('div','ratings-bar')
		rate=f'{rating.strong.text}/10'
		meta=star.span.text if (star:=rating.find('div',class_='inline-block ratings-metascore')) else "Oh ! my Meta_score"

		Divs=box.find_all('p',{'class':'text-muted'})
		certificate=cert.text.strip() if (cert:=Divs[0].find('span',class_='certificate')) else "Certificate seems to be lost"
		time=clock.text if (clock:=Divs[0].find('span',class_='runtime')) else "Time Seems to be unlimited?"
		genre=dress.text.strip() if (dress:=Divs[0].find('span',class_='genre')) else "Genre seems to be flying"
		summary=Divs[1].text.strip()

		ballot =box.find_all('span',{'name':"nv"})
		vote   =ballot[0].text
		gross  =ballot[1].text if len(ballot)>2 and '$' in ballot[1].text and '#' not in ballot[1].text  else "Still Collecting Cash"
		top_250=ballot[2].text if len(ballot)>2 and '#' in ballot[2].text and '$' not in ballot[2].text else "Can't be found in Top 250"
		
		with open("imdb_v5.csv",mode='a+',newline='') as editor:
			write=csv.writer(editor,delimiter=',')
			write.writerow([index,title,rate,year,time,genre,summary,vote,meta,gross,certificate,top_250])
		

imdb_v5(url)

