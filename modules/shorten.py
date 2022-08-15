import bitlyshortener
from configparser import ConfigParser
from termcolor import cprint
import colorama
import pyperclip
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
                pyperclip.copy(shorten)
                cprint(
                    f"Your shorten link is {shorten} and it's copied to clipboard just paste it !", 'green')
        except bitlyshortener.exc.RequestError:
            cprint(
                "Read the following error and act according to it.\n\nError: It might be one of these following error. \n 1. Invalid given URL \n 2. Invalid token\n 3. Network issue", 'red')
    else:
        cprint("Please provide the token", 'red')


process_it(input("Enter the url: ").split(" "))
