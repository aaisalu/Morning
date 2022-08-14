from amzqr import amzqr
import unicodedata
from termcolor import cprint
import colorama
import os
import re
import glob

colorama.init()


def beautify(info):
    # ver=input("What version would you like as QRcode output? [1-40]: ")
    # color=input("Do you love colors? [yes/no]: ")
    value = info, None, 'png', True, 10
    return roulette(value)


def folder(file):
    global Path
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    Path = rf"{desktop}\{file}"
    if not os.path.exists(Path):
        os.makedirs(Path)
    return Path


def getimg(string):
    path = r'..\gallery'
    if os.path.isdir(path):
        for k in glob.glob(rf'{path}\*.{string}'):
            return k, string
    else:
        cprint("Gallery folder can't be found in the Morning project folder", 'red')
        return None


def imageout(value):
    try:
        if not None is (storeimg := getimg('jpg')):
            cprint(
                f"\nProcessing output as {value[2]} with custom img.", 'green')
            return engine(value[0], storeimg[0], value[2], value[3], value[4])
        else:
            cprint(
                f"Picture isn't present in gallery folder so, processing {value[0][:10]}... output with {value[2]}", 'yellow')
            return engine(value[0], value[1], value[2], value[3], value[4])
    except OSError:
        cprint(
            "\nError: I can't produce color output in JPEG so, try changing it to png", 'red')


def gifout(value):
    try:
        if not None is (storegif := getimg('gif')):
            cprint(
                f"\nProcessing {value[0][:10]}... output as gif with custom img.", 'green')
            return engine(value[0], storegif[0], storegif[1], value[3], value[4])
        else:
            cprint(
                f"GIF isn't present in gallery folder so, processing {value[0][:10]}... output with {value[2]}", 'yellow')
            return engine(value[0], value[1], value[2], value[3], value[4])
    except OSError:
        cprint(
            "\nError: I can't produce color output in JPEG so, try changing it to png", 'red')


def chkreg(answer):
    return re.search("yes|1|yep|sure|True|yess|hellyeah|yeah", f'{answer}', flags=re.IGNORECASE)


def roulette(value):
    askimg = input("Do you want custom img or gif as output? [yes/no]: ")
    try:
        if chkreg(askimg):
            asktype = input("Do you want gif as output? [yes/no]: ")
            if chkreg(asktype):
                return gifout(value)
            else:
                return imageout(value)
        else:
            cprint(
                f"Processing {value[0][:10]}... output as {value[2]} without any custom img", 'yellow')
            return engine(value[0], value[1], value[2], value[3], value[3])

    except ValueError:
        cprint("\nError: Ohh snap!! Feels like my brain can't process this input", 'red')

# ::Thanks to S.Lott & martineau at stackoverflow.com/a/295466


def slugify(data, allow_unicode=False):
    """
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


def engine(info, img, ext, color, ver):
    version, level, qr_name = amzqr.run(
        info,
        version=ver,
        level='Q',
        picture=img,
        colorized=color,
        contrast=1.2,
        brightness=1.1,
        save_name=f'{slugify(info)[:15]}.{ext}',
        save_dir=folder("Qrcodes"))
    return cprint(f"\nSaved at {Path}", 'green')


beautify(str(input("Type anything which you want to convert it to QRcode: ")))
