from configparser import ConfigParser
from termcolor import cprint
import os
import colorama
import re
import unicodedata
import webbrowser
colorama.init()


def get_token(token_name):
    try:
        config = ConfigParser()
        config.read('../config.ini')
        data = config['API'][token_name]
        return data.strip()
    except KeyError:
        cprint("Please provide the token!", 'red')
        return None


def create_folder(file_name):
    global Path
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    try:
        Path = rf"{desktop}\{file_name}"
        if not os.path.exists(Path):
            os.makedirs(Path)
        return Path
    except:
        cprint('Error at creating folder... saving at default folder', 'red')
        Path = rf"{desktop}\Dropped_contents"
        if not os.path.exists(Path):
            os.makedirs(Path)
        return Path


def chkreg(answer):
    return re.search("yes|1|yep|sure|True|yess|hellyeah|yeah|r|refresh", f'{answer}', flags=re.IGNORECASE)


def slugify(data, allow_unicode=False):
    """
    Thanks to S.Lott & martineau at stackoverflow.com/a/295466
    Thanks for django dev code taken from https://github.com/django/django/blob/master/django/utils/text.py
    """
    data = str(data)
    if allow_unicode:
        data = unicodedata.normalize('NFKC', data)
    else:
        data = unicodedata.normalize('NFKD', data).encode(
            'ascii', 'ignore').decode('ascii')
    data = re.sub(r'[^\w\s-]', '', data.lower())
    return re.sub(r'[-\s]+', '-', data).strip('-_')


def view_file(filename):
    # Thanks to Máthé Endre-Botond at stackoverflow.com/a/6178200
    webbrowser.open(rf'{filename}')
    return cprint(f"\nSaved at {filename}", 'green')
