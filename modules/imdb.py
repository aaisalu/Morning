from bs4 import BeautifulSoup
from termcolor import cprint
import helper_func
import requests
import csv
import os
import re
import colorama
import sys
colorama.init()


def cheknet(url):
    try:
        incoming = requests.get(url)
        if incoming.status_code != 200:
            raise RuntimeError(
                "SOORY ERROR OUT due to excess Resonse Status over 200")
        cprint(f"\nServer Response : {incoming}", 'green')
        print('')
        return imdb_v5(incoming)
    except requests.exceptions.ConnectionError:
        cprint("\nHmmm…can't reach to the server", 'red')
        cprint("Please...Check your network connection.", 'red')


def imdb_v5(getdata):
    incoming = getdata.text
    soup = BeautifulSoup(incoming, 'lxml')
    data = soup.find_all('div', {"class": 'lister-item mode-advanced'})
    for index, box in enumerate(data):
        title = box.h3.a.text
        year = box.find(
            'span', class_='lister-item-year text-muted unbold').text.replace('(', '').replace(')', '')
        rating = box.find('div', 'ratings-bar')
        rate = f'{rating.strong.text}/10'
        meta = star.span.text if (star := rating.find(
            'div', class_='inline-block ratings-metascore')) else "Oh ! my Meta_score"
        Divs = box.find_all('p', {'class': 'text-muted'})
        certificate = cert.text.strip() if (cert := Divs[0].find(
            'span', class_='certificate')) else "Certificate seems to be lost"
        time = clock.text if (clock := Divs[0].find(
            'span', class_='runtime')) else "Time Seems to be unlimited?"
        genre = dress.text.strip() if (dress := Divs[0].find(
            'span', class_='genre')) else "Genre seems to be flying"
        summary = Divs[1].text.strip()
        ballot = box.find_all('span', {'name': "nv"})
        vote = ballot[0].text
        gross = ballot[1].text if len(
            ballot) > 2 and '$' in ballot[1].text and '#' not in ballot[1].text else "Still Collecting Cash"
        top_250 = ballot[2].text if len(
            ballot) > 2 and '#' in ballot[2].text and '$' not in ballot[2].text else "Can't be found in Top 250"
        with open(rf"{helper_func.create_folder('Moviez')}\Imdb_movies_lists.csv", mode='a+', newline='') as editor:
            write = csv.writer(editor, delimiter=',')
            write.writerow([index, title, rate, year, time, genre,
                           summary, vote, meta, gross, certificate, top_250])
    os.startfile(helper_func.Path)
    return cprint(f'Saved at {helper_func.Path}', 'green')


def checkbox(url):
    # Thanks to @prashant_srivastava at geeksforgeeks.org/check-if-an-url-is-valid-or-not-using-regular-expression for regex
    regex = ("((http|https)://)(www.)?" + "[a-zA-Z0-9@:%._\\+~#?&//=]"+"title|imdb|alpha|asc|runtime|year|release_date|your_rating_date|my_ratings|sort|search|num_votes|boxoffice_gross_us|top|count|user_rating|groups|adv_nxt" +
             "{2,256}\\.[a-z]" + "{2,6}\\b([-a-zA-Z0-9@:%" + "._\\+~#?&//=]*)")
    compiled = re.compile(regex, flags=re.IGNORECASE)
    if (url == None):
        cprint('Starting to Scrap Website by default link', 'yellow')
        return cheknet('https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc&count=100&start=%27+%27&ref_=adv_nxt')
    elif (re.search(compiled, url)):
        cprint("I'll crawl like spider! wait & watch", 'green')
        return cheknet(url)
    else:
        cprint('Starting to Scrap Website by default link', 'yellow')
        return cheknet('https://www.imdb.com/search/title/?groups=top_1000&sort=alpha,asc')


def main():
    try:
        print('')
        cprint("If you don't understand what the heck is this then simply press enter to scrap with default link", 'green')
        checkbox(str(input("Please provide the link of IMDb movies unsorted list: ")))
    except KeyboardInterrupt:
        print("Exiting from the script....")
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
