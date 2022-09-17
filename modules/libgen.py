from libgen_api.libgen_search import LibgenSearch
from tabulate import tabulate
import webbrowser
import helper_func
import colorama
from termcolor import cprint
import sys

colorama.init()
get_rawdata = LibgenSearch()

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
        resolved_download_links = get_rawdata.resolve_download_links(bit)
        resolved_get = resolved_download_links['GET']
        unique_id = bit['ID']
        Title = f"<a class='resolved_links' href={resolved_get} target='_blank'>{bit['Title']}</a>"
        Author = bit['Author']
        Publisher = bit['Publisher']
        Year = bit['Year']
        Pages = bit['Pages']
        Language = bit['Language']
        Size = bit['Size']
        Extension = bit['Extension']
        resolved_cloudfare = resolved_download_links['Cloudflare']
        resolved_ipfs = resolved_download_links['IPFS.io']
        Donwload_links = f"<a class='resolved_links' href={resolved_cloudfare} target='_blank'>Link 1</a></br><a class='resolved_links' href={resolved_ipfs} target='_blank'>Link 2</a>"
        Donwload_mirror = f"<a class='mirror_links' href={bit['Mirror_1']} target='_blank'>Mirror 1</a>&nbsp&nbsp<a class='mirror_links' href={bit['Mirror_2']} target='_blank'>Mirror 2</a></br><a class='mirror_links' href={bit['Mirror_3']} target='_blank'>Mirror 3</a>&nbsp&nbsp<a class='mirror_links' href={bit['Mirror_4']} target='_blank'>Mirror 4</a>"
        columns = unique_id, Title, Author, Publisher, Year, Pages, Language, Size, Extension, Donwload_links, Donwload_mirror
        body.append(columns)
    headers = ["ID", "Title", "Author", "Publisher", "Year",
               "Pages", "Language", "Size", "Extension", "Donwload Link", "Mirror Link"]
    formatted = tabulate(body, headers,  tablefmt="unsafehtml")
    html(formatted)


def adv_mode(title_book):
    book_filters=dict()
    cprint("\n\tNote: Press Enter to skip the section if you're unsure of the value\n",'green')
    try:
        year=input("In which year book was published ?: ")
        if len(year)>=3:
            book_filters.update({"Year": year})
    except:
        cprint('As the book, pubished year is not well defined so, excluding it.','yellow')
    try:
        book_filters.update({"Language": lang,}) if (lang:=input("Enter the language of the book: ").lower()) else book_filters.update({"Language": "English",})
        extension=input("Which file format would you like to choose? [pdf/epub]: ").lower()
        if extension in ['pdf', 'ext']:
            book_filters.update({"Extension": extension})
    except:
        cprint('Error selecting file format between pdf & epub so, excluding it.','yellow')
    if book_filters:
        cprint("\n\tNote: Turning on the strict match filter might show 0 results depending upon your filers..so press enter to skip the match section.\n",'yellow')
        exact_filter=True if helper_func.chkreg("",input("Do you want to enable strict match filters? [Y/N]: ")) else False
        adv_filter = get_rawdata.search_title_filtered(title_book, book_filters, exact_match=exact_filter)
        process_it(adv_filter)
    else:
       process_it(get_rawdata.search_title(title_book))

def ask_user():
    title_book= input("Enter the book title: ")
    if len(title_book)>=3:
        return adv_mode(title_book) if helper_func.chkreg("",(input('Do you want to enable advanced book search? [Y/N]: '))) else process_it(get_rawdata.search_title(title_book))
    cprint("Please enter at least 3 character book names!",'red')
    return ask_user()

def main():
    try:
        ask_user()
    except KeyboardInterrupt:
        print("Exiting from the script....")
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()