import bitlyshortener
from configparser import ConfigParser


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
                print(f'Your shorten link is {shorten}')
        except bitlyshortener.exc.RequestError:
            print("Looks like your input or the token is wrong")
    else:
        print("Please provide the token")


process_it(input("Enter the url: ").split(" "))
