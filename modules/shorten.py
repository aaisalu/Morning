import bitlyshortener
from configparser import ConfigParser
from termcolor import cprint
import colorama
colorama.init()


def get_token():
    tokens = []
    config = ConfigParser()
    config.read('../config.ini')
    data = config['API']['Bitly_token']
    if data:
        tokens.append(data.strip())
        return tokens
    return None


def process_it(url):
    if (api := (get_token())):
        try:
            shortener = bitlyshortener.Shortener(
                tokens=api, max_cache_size=256)
            for shorten in shortener.shorten_urls(url):
                cprint(f'Your shorten link is {shorten}', 'green')
        except bitlyshortener.exc.RequestError:
            cprint("Looks like your given URL or the token can't be verified", 'red')
    else:
        cprint("Please provide the token", 'red')


process_it(input("Enter the url: ").split(" "))
