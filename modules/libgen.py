from libgen_api.libgen_search import LibgenSearch
from tabulate import tabulate


title = "Pride and Prejudice"


def process_it(chunk):
    body = []
    for bit in chunk:
        unique_id = bit['ID']
        Author = bit['Author']
        Title = bit['Title']
        Publisher = bit['Publisher']
        Year = bit['Year']
        Pages = bit['Pages']
        Language = bit['Language']
        Size = bit['Size']
        Extension = bit['Extension']
        download_links = bit['Mirror_1']
        columns = unique_id, Title, Author, Publisher, Year, Pages, Language, Size, Extension, download_links
        body.append(columns)
    headers = ["ID", "Title", "Author", "Publisher", "Year",
               "Pages", "Language", "Size", "Extension", "Donwload Link"]
    print(tabulate(body, headers,  tablefmt="rst"))


t = LibgenSearch()
titles = t.search_title(title)

process_it(titles)
