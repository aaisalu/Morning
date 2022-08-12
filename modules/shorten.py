import bitlyshortener
from configparser import ConfigParser

config = ConfigParser()
config.read('config.cfg')
get_tokens = [config['API']['Bitly_token']]
shortener = bitlyshortener.Shortener(tokens=get_tokens, max_cache_size=256)

ask = str(input('Enter the url: '))
print(shortener.shorten_urls([ask]))
