from bs4 import BeautifulSoup
import requests,csv

url=input("Please feed the imdb website: ")
def imdb_v2(url):
	i=0
	pop=BeautifulSoup(requests.get(url).text,"lxml")
	Garage=pop.find_all('div',class_='lister-item mode-advanced')
	for Container in Garage:
		i+=1
		Title=Container.find('h3',{"class":'lister-item-header'}).a.text
		Year=Container.find('span',{'class':'lister-item-year text-muted unbold'}).text
		Genre=Container.find('span',class_='genre').text.strip()
		Time=Container.find('span',class_='runtime').text
		Certificate="Error Fetching Data" if Container.find('span',class_='certificate')==None else Container.find('span',class_='certificate').text 
		Ratebox=Container.find('div',class_='ratings-bar')
		Rate=Ratebox.find('span',class_='rating-rating').text
		Score="Data Not Found on Site " if Ratebox.find('span',class_='metascore favorable')==None else Ratebox.find('span',class_='metascore favorable').text
		Paragraph=Container.find_all('p',class_='text-muted')[1].text.strip()
		Votes=Container.find('p',class_='sort-num_votes-visible').find('span',{'name':'nv'}).text	
		Bank=Container.find_all('span',{'name':'nv'})
		Gross=Bank[1].text if len(Bank)>1 else "No any Data Found on Site "
		with open('Imdb_v2.csv' ,'a+') as k:
			pop=csv.writer(k,delimiter=',')
			pop.writerow([i,Title,Year,Genre,Time,Certificate,Rate,Score,Paragraph,Votes,Gross])
	
imdb_v2(url)