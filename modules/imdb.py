from bs4 import BeautifulSoup
import requests,csv
import os
import re


def folder(file):
    global Path
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
    Path=rf"{desktop}\{file}"
    if not os.path.exists(Path):
        os.makedirs(Path)
    return Path


def imdb_v5(url):
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
        
        with open(rf"{folder('Moviez')}\Imdb_movies_lists.csv",mode='a+',newline='') as editor:
            write=csv.writer(editor,delimiter=',')
            write.writerow([index,title,rate,year,time,genre,summary,vote,meta,gross,certificate,top_250])
        return print(f'Saved at {Path}')					

def checkbox(url):
    regex = ("((http|https)://)(www.)?" +"[a-zA-Z0-9@:%._\\+~#?&//=]"+"title|imdb|sort|search|top|count|user_rating|groups|adv_nxt" +"{2,256}\\.[a-z]" +"{2,6}\\b([-a-zA-Z0-9@:%" +"._\\+~#?&//=]*)")
    compiled = re.compile(regex,flags=re.IGNORECASE)
    if (url == None):
        print('Starting to Scrap Website by default link')  
        return imdb_v5('https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc&count=100&start=%27+%27&ref_=adv_nxt')
    elif (re.search(compiled, url)):
        print("I'll crawl like spider! wait & watch")  
        return imdb_v5(url)
    else:
        print('Starting to Scrap Website by default link')  
        return imdb_v5('https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc&count=100&start=%27+%27&ref_=adv_nxt')

print('')
print("If you don't understand what the heck is this then simply press enter to scrap with default link")
checkbox(str(input("Please provide the link of IMDb movies unsorted list: ")))
