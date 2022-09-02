from libgen_api.libgen_search import LibgenSearch
from tabulate import tabulate
import webbrowser

title = "Pride and Prejudice"


def html(data):
    htmls = f'''
<!DOCTYPE html>
<html lang="en" style="width:90%;">
<head>
<meta charset="UTF-8" />
<meta http-equiv="X-UA-Compatible" content="IE=edge" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Books</title>
</head>
<body>
{data}
</body>
</html>
'''
    with open("testdata.html", 'w') as kaka:
        kaka.write(htmls)
    webbrowser.open(r"testdata.html")


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
        resolved_download_links = t.resolve_download_links(bit)
        resolved_get = resolved_download_links['GET']
        resolved_cloudfare = resolved_download_links['Cloudflare']
        resolved_ipfs = resolved_download_links['IPFS.io']
        Donwload_links = f"<a class='resolved_links' href={resolved_get} target='_blank'>Link 1</a>&nbsp&nbsp<a class='resolved_links' href={resolved_cloudfare} target='_blank'>Link 2</a></br><a class='resolved_links' href={resolved_ipfs} target='_blank'>Link 3</a>"
        Donwload_mirror = f"<a class='mirror_links' href={bit['Mirror_1']} target='_blank'>Mirror 1</a>&nbsp&nbsp<a class='mirror_links' href={bit['Mirror_2']} target='_blank'>Mirror 2</a></br><a class='mirror_links' href={bit['Mirror_3']} target='_blank'>Mirror 3</a>&nbsp&nbsp<a class='mirror_links' href={bit['Mirror_4']} target='_blank'>Mirror 4</a>"
        columns = unique_id, Title, Author, Publisher, Year, Pages, Language, Size, Extension, Donwload_links, Donwload_mirror
        body.append(columns)
    headers = ["ID", "Title", "Author", "Publisher", "Year",
               "Pages", "Language", "Size", "Extension", "Donwload Link", "Mirror Link"]
    formatted = tabulate(body, headers,  tablefmt="unsafehtml")
    html(formatted)


t = LibgenSearch()
titles = t.search_title(title)

process_it(titles)
