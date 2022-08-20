from configparser import ConfigParser
from termcolor import cprint
import os
import colorama
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
