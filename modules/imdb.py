from bs4 import BeautifulSoup
import requests,csv

url=input("Please feed the imdb website: ")

def imdb_v4(url):
	# url='https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc&count=100&start=%27+str(hi)+%27&ref_=adv_nxt'
	# url='https://www.imdb.com/search/title/?count=100&groups=oscar_best_picture_winners&sort=year%2Cdesc&ref_=nv_ch_osc'
	incoming=requests.get(url).text
	parse=BeautifulSoup(incoming,'lxml')
	storage=parse.find_all('div',class_='lister-item mode-advanced')
	for data in storage:
		index=data.find('span','lister-item-index unbold text-primary').text
		title=data.h3.a.text
		year=data.h3.find('span',class_='lister-item-year text-muted unbold').text.replace('(','').replace(')','')

		ratings=data.find('div',class_='ratings-bar')
		rate=f"{ratings.strong.text}/10"
		meta_box=ratings.find('div',class_='inline-block ratings-metascore')
		meta=meta_box.span.text.strip() if meta_box else "Oh ! my Meta_score"
		
		Divs=data.find_all('p','text-muted')
		certify= cert.text if (cert:=(Divs[0].find('span',{"class":"certificate"}))) else "Certificate seems to be lost"
		time=Divs[0].find('span',{"class":"runtime"}).text.strip()
		genre=Divs[0].find('span',{"class":"genre"}).text.strip()
		summary=Divs[1].text.strip()

		vote=data.find_all("span",{"name":"nv"})[0].text
		gross_check=growth[1].text if len(growth:=(data.find_all("span",{"name":"nv"})))>1   else "Gross seems to be hidden"
		gross=gross_check if "#" not in gross_check else "Gross seems to be hidden"

		top_250= top[-1].text if len(top:=(data.find_all("span",{"name":"nv"})))>2 else "Error on Top 250"

		with open("imdb_v4.csv",mode='a+',newline='') as editor:
			write=csv.writer(editor,delimiter=',')
			write.writerow([index,title,rate,year,time,genre,summary,vote,meta,gross,certify,top_250])
		

imdb_v4(url)