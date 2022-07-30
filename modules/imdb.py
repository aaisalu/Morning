from bs4 import BeautifulSoup
import requests,csv

url=input("Please feed the imdb website: ")
def imdb_v3(url):
	# url='https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc&count=100&start=%27+str(hi)+%27&ref_=adv_nxt'
	info=requests.get(url).text
	soup=BeautifulSoup(info,'lxml')
	library=soup.find_all('div',class_='lister-item mode-advanced')
	for smol in library:
		index=smol.find('h3',class_='lister-item-header').span.text
		title=smol.find('h3',class_='lister-item-header').a.text
		year=smol.find('h3',class_='lister-item-header').find('span',{'class':"lister-item-year text-muted unbold"}).text.replace('(','').replace(')','')## OR [1:5]
		rating=f"{smol.find('div',class_='ratings-bar').strong.text}/10"
		votes=smol.find_all('p',class_='sort-num_votes-visible')[0].find('span',{'name':"nv"}).text

		Div_box=smol.find_all('p',class_='text-muted')
		time=Div_box[0].find(class_='runtime').text
		genre=Div_box[0].find(class_='genre').text.strip()
		summary=Div_box[1].text.strip()

		Meta_box=smol.find('div',class_="ratings-bar").find('div',class_='inline-block ratings-metascore')
		meta=Meta_box.span.text.strip() if Meta_box else "No Entry Found"
		
		Old_top=smol.find_all('span',{'name':'nv'})[-1].text
		Top_box=smol.find_all('span',{'name':"nv"})[-1].text
		top_250=Top_box.replace('#','') if '#' in Top_box else "Can't find in Top 250"
		
		Gross_box=smol.find_all('span',{'name':'nv'})
		Check_point=Gross_box[1].text if len(Gross_box)>1  else "No Entry Found"
		gross=Check_point if '#' not in Check_point else "No Entry Found"
		with open('Imdb_v3.csv',newline='',mode='a+') as hello:
			pop=csv.writer(hello,delimiter=',')
			pop.writerow([index,title,rating,year,time,genre,summary,votes,meta,top_250,gross])
		

imdb_v3(url)