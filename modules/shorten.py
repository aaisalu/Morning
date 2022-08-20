from termcolor import cprint
import helper_func
import bitlyshortener
import colorama
import pyperclip
import sys
colorama.init()


def process_it(url):
    api = [helper_func.get_token('Bitly_token')]
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
        sys.exit(1)

    except bitlyshortener.exc.ArgsError:
        cprint(f"Token looks fishy...check your token or API", 'red')
        sys.exit(1)


def main():
    try:
        process_it(input("Enter the url: ").split(" "))
    except KeyboardInterrupt:
        print("Exiting from the script....")
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
